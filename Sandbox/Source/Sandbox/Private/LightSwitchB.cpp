// Fill out your copyright notice in the Description page of Project Settings.


#include "LightSwitchB.h"
#include "Components/PointLightComponent.h"
#include "Components/SphereComponent.h"

// Sets default values
ALightSwitchB::ALightSwitchB()
{
 	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;

	// Set desired intensity of Point Light
	DesiredIntensity = 5000.0f;

	// Create point light
	PointLight1 = CreateDefaultSubobject<UPointLightComponent>(TEXT("PointLight1"));
	PointLight1->Intensity = DesiredIntensity;
	PointLight1->SetHiddenInGame(false);
	RootComponent = PointLight1;

	// Create sphere collider and set visibility in game
	Sphere1 = CreateDefaultSubobject<USphereComponent>(TEXT("Sphere1"));
	Sphere1->InitSphereRadius(250.0f);
	Sphere1->SetupAttachment(RootComponent);
	Sphere1->SetHiddenInGame(false);

	// Sets begin and end overlaps for sphere collider
	Sphere1-> OnComponentBeginOverlap.AddDynamic(this, &ALightSwitchB::OnOverlapBegin);
	Sphere1-> OnComponentEndOverlap.AddDynamic(this, &ALightSwitchB::OnOverlapEnd);
}

// Called when the game starts or when spawned
void ALightSwitchB::BeginPlay()
{
	Super::BeginPlay();
	
}

// Called every frame
void ALightSwitchB::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

}

void ALightSwitchB::OnOverlapBegin_Implementation(UPrimitiveComponent *OverlappedComp, AActor *OtherActor, UPrimitiveComponent *OtherComp, int32 OtherBodyIndex, bool bFromSweep, const FHitResult &SweepResult)
{
	if(OtherActor && (OtherActor != this) && OtherComp)
	{
		ToggleLight();
	}
}

void ALightSwitchB::OnOverlapEnd_Implementation(UPrimitiveComponent *OverlappedComp, AActor *OtherActor, UPrimitiveComponent *OtherComp, int32 OtherBodyIndex)
{
	if(OtherActor && (OtherActor != this) && OtherComp)
	{
		ToggleLight();
	}
}

void ALightSwitchB::ToggleLight()
{
	PointLight1->ToggleVisibility();
}