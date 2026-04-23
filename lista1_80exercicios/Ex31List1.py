codigo = int(input("digite o codigo do produto pedido: "))
quantidade = int(input("digite a quantidade do produto pedido: "))
if codigo == 100:
    preco = quantidade * 1.20
elif codigo == 101:
    preco = quantidade * 1.30
elif codigo == 102:
    preco = quantidade * 1.50
elif codigo == 103:
    preco = quantidade * 1.20
elif codigo == 104:
    preco = quantidade * 17
elif codigo == 105:
    preco = quantidade * 9.50
elif codigo == 106:
    preco = quantidade * 6
else:
    print ("codigo invalido")
print (f"valor final do pedido = {preco}")




