altura = float(input ("digite a altura: "))
letra = str(input ("digite F = feminino ou M = masculino :"))
if letra == 'M' or letra == 'm':
    peso = (72.7 * altura) - 58
    print (f"peso ideal e de {peso}.")
elif letra == 'F' or letra == 'f':
    peso = (62.1 * altura) - 44.7
    print (f"peso ideal e de {peso}.")
else:
    print ("Sexo invalido")


