// 

#include "ChatGPTWrapper.h"
#include "Dom/JsonObject.h"
#include "Serialization/JsonReader.h"
#include "Serialization/JsonSerializer.h"
#include "Misc/ConfigCacheIni.h"

UChatGPTWrapper::UChatGPTWrapper()
{
}

void UChatGPTWrapper::SetOpenAIAPIKey(const FString& APIKey)
{
    OpenAIAPIKey = APIKey;
}

FString UChatGPTWrapper::GetOpenAIAPIKey()
{
    if (!OpenAIAPIKey.IsEmpty())
    {
        return OpenAIAPIKey;
    }

    FString APIKey;
    if (GConfig->GetString(TEXT("OpenAI"), TEXT("APIKey"), APIKey, GEngineIni))
    {
        return APIKey;
    }
    return TEXT("");
}

//Send request to API using Json
void UChatGPTWrapper::SendRequest(const FString& Prompt, const FOnSuccessDelegate& OnSuccess, const FOnErrorDelegate& OnError)
{
    FString APIKey = GetOpenAIAPIKey();
    if (!APIKey.IsEmpty())
    {
        FHttpModule* Http = &FHttpModule::Get();
        TSharedRef<IHttpRequest, ESPMode::ThreadSafe> Request = Http->CreateRequest();
        Request->OnProcessRequestComplete().BindUObject(this, &UChatGPTWrapper::OnResponseReceived, OnSuccess, OnError);
        Request->SetURL("https://api.openai.com/v1/completions");
        Request->SetVerb("POST");
        Request->SetHeader("Content-Type", "application/json");
        Request->SetHeader("Authorization", FString::Printf(TEXT("Bearer %s"), *APIKey));

        TSharedPtr<FJsonObject> JsonRequestObject = MakeShareable(new FJsonObject);
        JsonRequestObject->SetStringField("prompt", Prompt);
        JsonRequestObject->SetNumberField("max_tokens", MaxTokens);
        JsonRequestObject->SetNumberField("temperature", Temperature);
        JsonRequestObject->SetNumberField("top_p", TopP);
        JsonRequestObject->SetStringField("model", "text-davinci-003");

        FString JsonPayload;
        TSharedRef<TJsonWriter<>> JsonWriter = TJsonWriterFactory<>::Create(&JsonPayload);
        FJsonSerializer::Serialize(JsonRequestObject.ToSharedRef(), JsonWriter);

        Request->SetContentAsString(JsonPayload);
        Request->ProcessRequest();

    }
    else
    {
        OnError.Execute(-1, TEXT("OpenAI API Key not found or invalid"));
    }
}

void UChatGPTWrapper::OnResponseReceived(FHttpRequestPtr Request, FHttpResponsePtr Response, bool bWasSuccessful, FOnSuccessDelegate OnSuccess, FOnErrorDelegate OnError)
{
    if (bWasSuccessful && Response.IsValid())
    {
        if (Response->GetResponseCode() == 200)
        {
            TSharedPtr<FJsonObject> JsonObject;
            TSharedRef<TJsonReader<>> Reader = TJsonReaderFactory<>::Create(Response->GetContentAsString());

            if(FJsonSerializer::Deserialize(Reader, JsonObject))
            {
                TArray<TSharedPtr<FJsonValue>> Choices = JsonObject->GetArrayField("choices");
                if (Choices.Num() > 0)
                {
                    TSharedPtr<FJsonObject> ChoiceObject = Choices[0]->AsObject();
                    FString GeneratedText = ChoiceObject->GetStringField("text");

                    OnSuccess.Execute(GeneratedText);
                }
                else
                {
                    OnError.Execute(Response->GetResponseCode(), TEXT("No choices were returned by the API"));
                }
            }
            else
            {
                OnError.Execute(Response->GetResponseCode(), TEXT("Failed to parse the JSON response"));
            }
        }
        else
        {
            OnError.Execute(Response->GetResponseCode(), FString::Printf(TEXT("API returned an error. Response code: %d"), Response->GetResponseCode()));
        }
    }
    else
    {
        OnError.Execute(-1, TEXT("Failed to connect to the OpenAI API"));
    }
}