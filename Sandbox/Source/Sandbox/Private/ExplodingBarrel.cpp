// Fill out your copyright notice in the Description page of Project Settings.


#include "ExplodingBarrel.h"
#include "Components/StaticMeshComponent.h"
#include "Particles/ParticleSystemComponent.h"
#include "Kismet/GameplayStatics.h"
#include "TimerManager.h"

// Sets default values
AExplodingBarrel::AExplodingBarrel()
{
 	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;

	BarrelMesh = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("BarrelMesh"));
	RootComponent = BarrelMesh;

	FireParticleSystemComponent = CreateDefaultSubobject<UParticleSystemComponent>(TEXT("BarrelMeshFireParticle"));
	FireParticleSystemComponent->SetupAttachment(RootComponent);
	FireParticleSystemComponent->bAutoActivate = false;

	RadialForce = CreateDefaultSubobject<URadialForceComponent>(TEXT("RadialForce"));

	RadialForce->Radius = ExplosionRadius;
	RadialForce->bImpulseVelChange = true;
	RadialForce->bAutoActivate = false;
	RadialForce->bIgnoreOwningActor = false;

	OnTakeAnyDamage.AddDynamic(this,&AExplodingBarrel::OnDamageTaken);

	HitPoints = 10.0f;
	ExplosionDamage = 10.0f;
	ExplosionRadius = 200.0f;


}

// Called when the game starts or when spawned
void AExplodingBarrel::BeginPlay()
{
	Super::BeginPlay();
	
}

// Called every frame
void AExplodingBarrel::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

}

void AExplodingBarrel::OnDamageTaken(AActor *DamagedActor, float Damage, const UDamageType *DamageType, AController *InstigatedBy, AActor *DamageCauser)
{
	if(Damage > 0.f && HitPoints > 0.f)
	{
		HitPoints-= Damage;
		UE_LOG(LogTemp, Warning, TEXT("Damage taken, Hitpoints: %f"), HitPoints); //log the remaining hitpoints

		// Start the fire particle system
		if(!FireParticleSystemComponent->IsActive())
		{
			FireParticleSystemComponent->Activate();
		}

		// Start a countdown if not started
		if(!GetWorld()->GetTimerManager().IsTimerActive(CountdownTimerHandle))
		{
			UE_LOG(LogTemp, Warning, TEXT("Setting countdown timer")); // Log if the timer is being set
			GetWorld()->GetTimerManager().SetTimer(CountdownTimerHandle, this, &AExplodingBarrel::Countdown, 1.0f, true);
		}
	}

	// If hitpoints reach 0, the barrel explodes
	if(HitPoints<= 0.f)
	{
		// Stop fire particle system
		if(FireParticleSystemComponent!= nullptr)
		{
			FireParticleSystemComponent->Deactivate();
		}

		// Cache location for spawning events
		FVector BarrelLocation = GetActorLocation();

		Destroy();

		UGameplayStatics::ApplyRadialDamage(this, ExplosionDamage, BarrelLocation, ExplosionRadius, nullptr, TArray<AActor*>(), this);

		if(RadialForce != nullptr)
		{
			RadialForce->FireImpulse();
		}

		// Play explosion sound and particle system
		UGameplayStatics::SpawnEmitterAtLocation(GetWorld(), ExplosionParticle, BarrelLocation);
		UGameplayStatics::PlaySoundAtLocation(GetWorld(), ExplosionSound, BarrelLocation);

		Destroy();
	}
}

void AExplodingBarrel::Countdown()
{
	HitPoints--;
	UE_LOG(LogTemp, Warning, TEXT("Coundown called, Hitpoints: %f"), HitPoints); // log when the countdown function is called and the remaining hitpoints

	// If hitpoints reach 0, the barrel explodes
	if(HitPoints <= 0.f)
	{
		OnDamageTaken(this, 0.0f, nullptr, nullptr, nullptr);
	}
}