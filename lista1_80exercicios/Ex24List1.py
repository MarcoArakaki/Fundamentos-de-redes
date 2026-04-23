num1 = int(input("digite o tamanho do primeiro lado do triangulo: "))
num2 = int(input("digite o tamanho do segundo lado do triangulo: "))
num3 = int(input("digite o tamanho do terceiro lado do triangulo: "))
if num1 < (num2 + num3) and num2 < (num1+num3) and num3 <(num1 + num2):
    if num1 == num2 == num3:
        print ("triangulo equilatero")
    elif num1 != num2 !=num3:
        print ("triangulo escaleno")
    else:
        print ("triangulo isosceles")
else:
    print ("valor invalido")


