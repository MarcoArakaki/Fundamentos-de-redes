cont = 0
contp = 0
num = int(input("digite um numero: "))
while (num != 0):
    if num % 2 == 0:
        contp = contp + 1
        cont = cont + 1
        num = int(input("digite um numero: "))
    else:
        cont = cont +1
        num = int(input("digite um numero: "))
print (f"foram digitados {cont} numeros no total")
print (f"foram digitados {contp} numeros pares") 


