venda = float(input ("digite o valor de venda: "))
if venda >= 100000:
    res = (venda * 0.16) + 700
elif venda < 100000 and venda >= 80000:
    res = (venda * 0.14) + 650
elif venda < 80000 and venda >= 60000:
    res = (venda * 0.14) + 600
elif venda < 60000 and venda >= 40000:
    res = (venda * 0.14) + 550
elif venda < 40000 and venda >= 20000:
    res = (venda * 0.14) + 500
else:
    res = (venda * 0.14) + 400
print (f"comicao final e = {res}")