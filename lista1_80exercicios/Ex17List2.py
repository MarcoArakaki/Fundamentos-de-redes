quant = int(input("digite a quantidade de numeros a serem lidos: "))
maior = -999999999
for i in range (1, quant+1, 1):
    num = int(input(f"digite o {i}º numero: "))
    if num > maior:
        maior = num
print (f"o maior numero digitado e = {maior}")
