import math

x1 = float(input("Ponto A x: "))
y1 = float(input("Ponto A y: "))

x2 = float(input("Ponto B x: "))
y2 = float(input("Ponto B y: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"d = {distancia:.2f}")