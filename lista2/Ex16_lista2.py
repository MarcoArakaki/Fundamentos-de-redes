def consumo(potencia_watts, horas):
    consumo_kwh = (potencia_watts * horas) / 1000
    return consumo_kwh


potencia = 1500
tempo = 3

cons = consumo(potencia, tempo)

print(f"Consumo: {cons:.2f} kWh")