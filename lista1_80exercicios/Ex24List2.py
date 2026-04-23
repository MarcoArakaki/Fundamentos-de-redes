soma = 0
qtd = 0

while True:
    idade = int(input("Digite a idade e digite 0 para encerrar: "))
    if idade == 0:
        break 
    if idade < 0:
        print("Idade inválida, tente novamente!")
        continue
    soma += idade
    qtd += 1
media = soma / qtd
print(f"Quantidade de pessoas: {qtd}")
print(f"Idade média do grupo: {media:.2f} anos")
