valor = int(input ("digite o valor de venda: "))
print ("selecione o estado destino")
print ("1 para MG")
print ("2 para SP")
print ("3 para RJ")
print ("4 para MS")
estado = int(input (" . "))
if estado == 1:
    valorf = valor * 1.07
    print (f" o valor final do produto e de : {valorf}")
elif estado == 2:
    valorf = valor * 1.12
    print (f" o valor final do produto e de : {valorf}")
elif estado == 3:
    valorf = valor * 1.15
    print (f" o valor final do produto e de : {valorf}")
elif estado == 4:
    valorf = valor * 1.08
    print (f" o valor final do produto e de : {valorf}")
else:
    print ("estado invalido")