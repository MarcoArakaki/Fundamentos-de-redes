def imprimir_lista(lista):
    for i, valor in enumerate(lista, start=1):
        print(f"{i}, {valor}")

frutas = ["limao", "Uva", "jaca", "Salada"]
imprimir_lista(frutas)