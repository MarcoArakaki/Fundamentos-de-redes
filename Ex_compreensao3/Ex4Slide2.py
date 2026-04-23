def calcular_consumo(potencia_watts, tempo_horas):

    consumo_kwh = (potencia_watts * tempo_horas) / 1000
    return consumo_kwh

def calcular_conta(consumo_kwh, valor_kwh):
    return consumo_kwh * valor_kwh

potencia = 1500  
tempo = 3        
valor_kwh = 0.75

consumo = calcular_consumo(potencia, tempo)
conta = calcular_conta(consumo, valor_kwh)

print(f"Consumo: {consumo:.2f} kWh")
print(f"Valor da conta: R$ {conta:.2f}")