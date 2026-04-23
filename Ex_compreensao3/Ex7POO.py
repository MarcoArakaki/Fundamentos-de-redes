import math

class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def calcular_perimetro(self):
        return self.ladoA + self.ladoB + self.ladoC

    def get_maior_lado(self):
        return max(self.ladoA, self.ladoB, self.ladoC)

    def calcular_area(self):
        p = self.calcular_perimetro() / 2
        area = math.sqrt(p * (p - self.ladoA) * (p - self.ladoB) * (p - self.ladoC))
        return area


ladoA = float(input("Informe o lado A: "))
ladoB = float(input("Informe o lado B: "))
ladoC = float(input("Informe o lado C: "))

triangulo = Triangulo(ladoA, ladoB, ladoC)

print(f"Perímetro do triângulo: {triangulo.calcular_perimetro():.2f}")
print(f"Maior lado do triângulo: {triangulo.get_maior_lado():.2f}")
print(f"Área do triângulo: {triangulo.calcular_area():.2f}")