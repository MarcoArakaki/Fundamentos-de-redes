preco = float(input ("digite o valor do produto: "))
if preco < 50:
    res = preco * 1.05
elif preco >=50 and preco < 100:
    res = preco * 1.10
else:
    res = preco * 1.15
print (f"o preco final e = {res}")