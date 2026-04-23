menor = int(input ("digite a base menor (maior que zero): "))
maior = int(input ("digite a base maior (maior que zero): "))
altura = float (input ("digite a altura: "))
if maior > 0 and menor > 0:
    area = ((maior + menor)*altura)/2
    print (f"a area do trapezio e = {area}")
else:
    print ("valor invalido")


