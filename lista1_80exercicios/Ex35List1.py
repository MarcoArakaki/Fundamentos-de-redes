custof = float(input("digite o custo de fabrica: "))
if custof < 12000:
    dist = custof * 0.05
    imp = 0
elif custof >= 12000 and custof < 25000:
    dist = custof * 0.10
    imp = custof * 0.15
else:
    dist = custof * 0.15
    imp = custof * 0.20
custoc = custof + dist + imp
print (f"o custo final para o consumidor = {custoc}")