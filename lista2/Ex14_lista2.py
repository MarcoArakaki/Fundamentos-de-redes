def potencia(X, Z):
    resultado = 1
    if Z == 0:
        return 1
    elif Z > 0:
        for _ in range(Z):
            resultado *= X
    else:
        for _ in range(-Z):
            resultado *= X
        resultado = 1 / resultado
    return resultado

print(potencia(2, 3))