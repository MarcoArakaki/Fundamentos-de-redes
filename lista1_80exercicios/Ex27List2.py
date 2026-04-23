maior = -999999999
menor = 99999999
while True:
    n = int(input("Digite um numero inteiro e digite negativo para encerrar: "))
    
    if n < 0:
        break  # sai do loop
    
    if n > maior:
        maior = n
    if n < menor:
        menor = n

if maior is None:
    print("Nenhum numero válido foi digitado.")
else:
    print(f"Maior numero lido: {maior}")
    print(f"Menor numero lido: {menor}")