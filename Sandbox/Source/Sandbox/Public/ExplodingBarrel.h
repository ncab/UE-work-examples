#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Components/StaticMeshComponent.h"
#include "Sound/SoundCue.h"
#include "PhysicsEngine/RadialForceComponent.h"
#include "ExplodingBarrel.generated.h"

UCLASS(Blueprintable)
class SANDBOX_API AExplodingBarrel : public AActor
{
	GENERATED_BODY()
	
public:	
	// Sets default values for this actor's properties
	AExplodingBarrel();

protected:
	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Components")
	UStaticMeshComponent* BarrelMesh;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "ExplodingBarrel")
	float HitPoints;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "ExplodingBarrel")
	float ExplosionDamage;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "ExplodingBarrel")
	float ExplosionRadius;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "ExplodingBarrel")
	USoundCue* ExplosionSound;

	UPROPERTY(EditAnywhere, Category = "Effects")
	UParticleSystem* ExplosionParticle;

	UPROPERTY(VisibleAnywhere, Category = "Effects")
	UParticleSystemComponent* FireParticleSystemComponent;

	/*
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "ExplodingBarrel")
	UParticleSystem* FireParticle;
	*/

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Effects")
	URadialForceComponent* RadialForce;

	UFUNCTION()
	void OnDamageTaken(AActor* DamagedActor, float Damage, const class UDamageType* DamageType, AController* InstigatedBy, AActor* DamageCauser);

	FTimerHandle CountdownTimerHandle;

	void Countdown();

public:	
	// Called every frame
	virtual void Tick(float DeltaTime) override;

};
