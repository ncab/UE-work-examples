// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Test02.generated.h"

UCLASS()
class SANDBOX_API ATest02 : public AActor
{
	GENERATED_BODY()
	
public:	
	// Sets default values for this actor's properties
	ATest02();

protected:
	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

public:	
	// Called every frame
	virtual void Tick(float DeltaTime) override;

};
