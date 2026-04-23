def somar_argumentos(*args):
    return sum(args)

resultado1 = somar_argumentos(1, 2, 3, 4, 5)
print(f"Soma: {resultado1}")

resultado2 = somar_argumentos(10, 20)
print(f"Soma: {resultado2}") 