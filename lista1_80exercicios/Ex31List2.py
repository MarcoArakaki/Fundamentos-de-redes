numeros = []
pares = []
impares = []
print("Digite 20 números inteiros:")
for i in range(20):
    while True:
        try:
            numero_str = input(f"Digite o {i+1}º número: ")
            numero = int(numero_str)
            numeros.append(numero)
            if numero % 2 == 0:
                pares.append(numero)
            else:
                impares.append(numero)
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
print("\n--- Listas ---")
print(f"Todos os números: {numeros}")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")