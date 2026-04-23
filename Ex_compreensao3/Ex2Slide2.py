def calcular_media(lista):
    if len(lista) == 0:
        return 0
    soma = sum(lista)
    media = soma / len(lista)
    return media

numeros = [10, 20, 30, 40, 50]
resultado = calcular_media(numeros)
print(f"A média dos valores é: {resultado}")