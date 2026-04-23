def eh_primo(num):
    if num < 2:
        return False 
    for i in range(2, int(num**0.5) + 1): 
        if num % i == 0:
            return False  
    return True
def soma_n_primeiros_primos(n):
    if n <= 0:
        return 0

    soma_primos = 0
    contador_primos = 0
    numero_atual = 2

    while contador_primos < n:
        if eh_primo(numero_atual):
            soma_primos += numero_atual
            contador_primos += 1
        numero_atual += 1
    return soma_primos

try:
    n_input = int(input("Digite um número inteiro não negativo (n): "))
    if n_input < 0:
        print("Por favor, digite um número não negativo.")
    else:
        resultado = soma_n_primeiros_primos(n_input)
        print(f"A soma dos {n_input} primeiros números primos é: {resultado}")
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")