num1 = int(input ("Digite o 1 número: "))
num2 = int(input ("Digite o 2 número: "))
somap = 0
mult = 1
if num1 < num2:
    num = num1
    for num in range (num1, num2, +1):
        if num % 2 == 0:
            somap = somap + num
        else:
            mult = mult * num
else:
    num = num2
    for num in range (num2, num1, +1):
        if num % 2 == 0:
            somap = somap + num
        else:
            mult = mult * num
print (f"soma dos numeros pares no intervalo = {somap}")
print (f"multiplicacao dos numeros impares = {mult}")
