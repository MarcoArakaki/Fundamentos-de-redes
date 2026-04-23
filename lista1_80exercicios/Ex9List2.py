i = 0
maior = -9999999
menor = 99999999
for i in range (0, 10, 1):
    num = int(input ("digite um numero: "))
    if num > maior:
        maior = num  
    if num < menor:
        menor = num   
print (f"o menor dos numeros e = {menor}")
print (f"o maior dos numeros e = {maior}")
