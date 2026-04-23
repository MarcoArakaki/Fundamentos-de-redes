import math

while True:
    valor = float(input("Digite um valor (ou um negativo/zero para finalizar): "))

    if valor <= 0:
        break  

    quadrado = valor ** 2
    cubo = valor ** 3
    if valor >= 0:
        raiz_quadrada = math.sqrt(valor)
    else:
        raiz_quadrada = "Valor negativo"

    print(f"Valor: {valor}")
    print(f"Quadrado: {quadrado}")
    print(f"Cubo: {cubo}")
    print(f"Raiz Quadrada: {raiz_quadrada}")
    print("-" * 20)