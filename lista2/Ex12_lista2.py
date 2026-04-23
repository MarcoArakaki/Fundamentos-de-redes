import math

def calcularTempo(minutos):
    if minutos < 15:
        return 0.0
    else:
        horas = math.ceil(minutos / 60)
        if horas <= 1:
            return 9.0 
        else:
            return 9.0 + (horas - 1) * 1.5

print(calcularTempo(108))