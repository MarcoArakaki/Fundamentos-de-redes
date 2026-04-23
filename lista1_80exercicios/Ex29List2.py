numeros_digitados = []
soma_total = 0
print("Por favor, insira 5 números:")
for i in range(5):
    while True:
        try:
            numero_str = input(f"Digite o {i+1}º número: ")
            numero = float(numero_str)
            numeros_digitados.append(numero)
            soma_total += numero
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
print(f"\nA soma dos números é: {soma_total}")
print("\nOs números que você digitou foram:")
for numero in numeros_digitados:
    print(numero)