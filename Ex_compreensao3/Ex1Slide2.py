def salada_frutas(lista):
    for indice, elemento in enumerate(lista, start=1):
        print(f"{indice}, {elemento}")

frutas = ["Pera", "Uva", "Maça", "Salada mista"]
salada_frutas(frutas)