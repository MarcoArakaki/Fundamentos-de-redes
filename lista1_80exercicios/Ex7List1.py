compra = int(input ("digite o valor de compra: "))
if compra < 50:
    venda = compra * 1.45
    print (f"o valor de venda e {venda} com 45% de lucro")
else:
    venda = compra * 1.30
    print (f"o valor de venda e {venda} com 30% de lucro")
