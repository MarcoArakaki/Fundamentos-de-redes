numero_str = input("Por favor, insira um número inteiro maior do que zero: ")

try:
    numero = int(numero_str)
except ValueError:
    print("Número inválido")
    exit()

if numero <= 0:
    print("Número inválido")
else:
    soma_algarismos = 0
    temp_numero = numero
    while temp_numero > 0:
        algarismo = temp_numero % 10
        soma_algarismos += algarismo
        temp_numero //= 10
    print(f"A soma dos algarismos de {numero} é: {soma_algarismos}")