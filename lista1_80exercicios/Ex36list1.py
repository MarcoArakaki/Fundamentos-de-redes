peso = float (input ("digite o peso em kg: "))
altura = float (input ("digite a altura em metros:"))
imc = peso / (altura * altura)
if imc < 18.5:
    print ("abaixo do peso")
elif imc >18.5 and imc <25:
    print ("saudavel")
elif imc >= 25 and imc < 30:
    print ("peso em excesso")
elif imc >= 30 and imc < 35:
    print ("obesidade grau I")
elif imc >= 35 and imc < 40:
    print ("obesidade grau II(severa)")
else:
    print("obesidade grau III(morbida)")
