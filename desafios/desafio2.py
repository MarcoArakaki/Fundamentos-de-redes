comprimento_cm = float(input("Digite o comprimento da piscina (em centímetros): "))
largura_cm = float(input("Digite a largura da piscina (em centímetros): "))
profundidade_cm = float(input("Digite a profundidade da piscina (em centímetros): "))

comprimento_m = comprimento_cm / 100
largura_m = largura_cm / 100
profundidade_m = profundidade_cm / 100

volume_m3 = comprimento_m * largura_m * profundidade_m

litros = volume_m3 * 1000

print(f"Volume = {volume_m3:.1f} m³")
print(f"{int(litros):,} Litros")