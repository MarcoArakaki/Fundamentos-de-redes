import math

def calcularTempo(minutos):
    if minutos < 15:
        return 0.0
    elif minutos <= 60:
        return 9.0
    else:
        horas_adicionais = math.ceil((minutos - 60) / 60)  
        return 9.0 + (horas_adicionais * 1.5)

print("10 min → R$", calcularTempo(10))

import math

def calcularTempo(minutos):
    if minutos < 15:
        valor = 0.0
    elif minutos <= 60:
        valor = 9.0
    else:
        horas_adicionais = math.ceil((minutos - 60) / 60)
        valor = 9.0 + (horas_adicionais * 1.5)

    pis = valor * 0.0033
    cofins = valor * 0.0020
    icms = valor * 0.17
    total_impostos = pis + cofins + icms
    valor_final = valor + total_impostos

    print("===== RECIBO ESTACIONAMENTO =====")
    print(f"Tempo utilizado: {minutos} minutos")
    print(f"Valor base: R$ {valor:.2f}")
    print(f"PIS (0,33%): R$ {pis:.2f}")
    print(f"COFINS (0,20%): R$ {cofins:.2f}")
    print(f"ICMS (17%): R$ {icms:.2f}")
    print(f"Total de Impostos: R$ {total_impostos:.2f}")
    print(f"Valor Final a Pagar: R$ {valor_final:.2f}")
    print("=================================")

    return valor_final