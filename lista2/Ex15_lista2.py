def media_lista(lista):
    if len(lista) == 0:
        return 0
    soma = 0
    for valor in lista:
        soma += valor
    return soma / len(lista)

print(media_lista([10, 5, 90, 40]))