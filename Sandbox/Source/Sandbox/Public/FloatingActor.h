#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "FloatingActor.generated.h"

UCLASS()
class SANDBOX_API AFloatingActor : public AActor
{
	GENERATED_BODY()
	
public:	
	// Sets default values for this actor's properties
	AFloatingActor();

	// Define Static Mesh Component
	UPROPERTY(VisibleAnywhere)
	UStaticMeshComponent* FloatMesh;

	// Define float speed
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category= "FloatingActor")
	float FloatSpeed = 20.0f;

	// Define rotation speed
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category= "FloatingActor")
	float RotationSpeed = 20.0f;
	
protected:
	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

public:	
	// Called every frame
	virtual void Tick(float DeltaTime) override;

};
