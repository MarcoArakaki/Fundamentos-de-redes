a = float(input("digite o valor de a: "))
b = float(input("digite o valor de b: "))
c = float(input("digite o valor de c: "))
delta = (b**2) -4 * a * c
if a == 0:
    print ("A variável a tem que ser diferente de zero")
    quit
elif delta < 0:
    print ("nao existe raiz")
elif delta == 0:
    x = -b / (2 * a)
    print (f"raiz unica = {x}")
else:
    x1 = (-b + (delta**0.5)) / (2 * a)
    x2 = (-b - (delta**0.5)) / (2 * a)
    print (f"x1 = {x1} e x2 = {x2}")
