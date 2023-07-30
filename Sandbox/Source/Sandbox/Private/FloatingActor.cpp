// Fill out your copyright notice in the Description page of Project Settings.


#include "FloatingActor.h"

// Sets default values
AFloatingActor::AFloatingActor()
{
 	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;

	// Create Static Mesh Component and attach to Root
	FloatMesh = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("Static Mesh"));
	FloatMesh->SetupAttachment(RootComponent);

	static ConstructorHelpers::FObjectFinder<UStaticMesh> MeshAsset(TEXT("/Game/StarterContent/Shapes/Shape_Cube.Shape_Cube"));

	// If Mesh Asset is found, attach to root and set location to 0 in x, y, and z.
	if(MeshAsset.Succeeded())
		FloatMesh->SetStaticMesh(MeshAsset.Object);
		FloatMesh->SetRelativeLocation(FVector(0.0f, 0.0f, 0.0f));
}

// Called when the game starts or when spawned
void AFloatingActor::BeginPlay()
{
	Super::BeginPlay();
	
}

// Called every frame
void AFloatingActor::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

	// Define Actor Location and Rotation variables
	FVector NewLocation = GetActorLocation();
	FRotator NewRotation = GetActorRotation();

	// Define Running Time
	float RunningTime = GetGameTimeSinceCreation();

	// Add Sin Math to DeltaHeight
	float DeltaHeight = (FMath::Sin(RunningTime + DeltaTime) - FMath::Sin(RunningTime));

	//Add DeltaHeight to Z direction * float speed
	NewLocation.Z += DeltaHeight * FloatSpeed;

	// Add rotation to yaw * rotation speed
	float DeltaRotation = DeltaTime * RotationSpeed;
	NewRotation.Yaw += DeltaRotation;

	// Set Actor Location and Rotation
	SetActorLocationAndRotation(NewLocation, NewRotation);

}

