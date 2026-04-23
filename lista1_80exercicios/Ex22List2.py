n = int(input("Digite um número inteiro: "))
soma = 0
for i in range(1, n):
    if n % i == 0:
        soma += i
print(f"Soma dos divisores de {n}= {soma}")
