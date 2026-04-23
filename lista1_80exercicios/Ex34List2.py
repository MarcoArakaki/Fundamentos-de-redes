import math

def verificar_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True 
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True
numero_digitado = int(input("Digite um número inteiro maior que 1: "))
if verificar_primo(numero_digitado):
    print(f"O número {numero_digitado} é primo.")
else:
    print(f"O número {numero_digitado} não é primo.")