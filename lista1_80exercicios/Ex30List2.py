vetor_numeros = []
print("Por favor, insira 10 números inteiros:")
for i in range(10):
    while True:
        try:
            num = int(input(f"Digite o {i+1}º número: "))
            vetor_numeros.append(num)
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
while True:
    try:
        valor_procurado = int(input("Digite o valor que deseja procurar no vetor: "))
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
if valor_procurado in vetor_numeros:
    print(f"O valor {valor_procurado} foi encontrado no vetor.")
else:
    print(f"O valor {valor_procurado} não foi encontrado no vetor.")