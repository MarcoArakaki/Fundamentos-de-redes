def consumo_carro(distancia_km, litros_gastos):
    if litros_gastos == 0:
        return "Erro: litros consumidos não podem ser zero!"
    
    consumo = distancia_km / litros_gastos
    if consumo < 8:
        mensagem = "Gasta muito!"
    elif 8 <= consumo <= 15:
        mensagem = "Econômico!"
    else:
        mensagem = "Super econômico!"
    
    return f"Consumo: {consumo:.2f} Km/l - {mensagem}"

print(consumo_carro(100, 20))