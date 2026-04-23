km = float(input ("digite a distancia em km percorridos: "))
comb = float(input ("digite em litros o combustivel utilizado: "))
teste = km / comb
if teste < 8:
    print ("venda o carro")
elif teste >=8 and teste < 14:
    print ("economico")
else:
    print ("super economico")
