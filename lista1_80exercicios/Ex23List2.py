soma = 0
for i in range (0, 1000, 1):
    if i % 3:
        soma = soma + i
    elif i % 5:
        soma = soma + i
print (f"a soma de todos o numeros naturais abaixo de 1000 que são multiplos de 3 ou 5 sao {soma}")