num1 = int(input ("digite o 1 numero: "))
num2 = int(input ("digite o 2 numero: "))
if num1 > num2:
    print ("o numero 1 e maior que o numero 2")
    dif = num1 - num2
    print (f"a diferenca entre o 1 e o 2 numero e de : {dif} ")
elif num2 > num1:
    print ("o numero 2 e maior que o numero 1")
    dif = num2 - num1
    print (f"a diferenca entre o 2 e o 1 numero e de : {dif} ")
else:
    print ("os dois numeros sao iguais")
