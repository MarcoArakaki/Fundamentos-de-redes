print ("selecione o tipo de operacao que deseja usar")
print ("1 para operacao de soma")
print ("2 para operacao de subtracao")
print ("3 para operacao de multiplicacao")
print ("4 para operacao de divisao")
operacao = int(input(" . "))
if operacao == 1:
    num1 = int(input("digite o primeiro numero: "))
    num2 = int(input("digite o segundo numero: "))
    res = num1 + num2
    print (f"o valo da soma de {num1} + {num2} = {res}")
elif operacao == 2:
    num1 = int(input("digite o primeiro numero: "))
    num2 = int(input("digite o segundo numero: "))
    res = num1 - num2
    if res < 0:
                res = res * -1
    print (f"o valo da subtracao e = {res}")
elif operacao == 3:
    num1 = int(input("digite o primeiro numero: "))
    num2 = int(input("digite o segundo numero: "))
    res = num1 * num2
    print (f"o valo da multiplicacao de {num1} x {num2} = {res}")
elif operacao == 4:
    num1 = int(input("digite o numero: "))
    num2 = int(input("digite o denominador: "))
    if num2 != 0:
        res = num1 / num2
        print (f"o valo da divisao de {num1} / {num2} = {res}")
    else:
         print ("denominado precisa ser diferente de 0")
else:
    print ("valor da opecacao invalido")