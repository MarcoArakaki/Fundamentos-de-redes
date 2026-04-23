i = 0
soma = 0
cont = 0
for i in range (0, 10, 1):
    num = int(input ("digite um numero: "))
    if num >0:
        soma = soma + num
        cont = cont +1    
res = soma /cont
print (f"a media dos numeros positivos e = {res}")
