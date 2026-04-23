def calcular_multa(peso_peixes):
    limite = 50
    multa_por_kg = 4.0
    
    if peso_peixes > limite:
        excesso = peso_peixes - limite
        multa = excesso * multa_por_kg
    else:
        excesso = 0
        multa = 0.0
    
    print(f"Peso total de peixes: {peso_peixes} Kg")
    print(f"Excesso: {excesso} Kg")
    print(f"Multa a pagar: R$ {multa:.2f}")
    
    return excesso, multa