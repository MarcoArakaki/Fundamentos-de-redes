def calcular_salario(horas_trabalhadas, valor_hora):
    if horas_trabalhadas <= 40:
        salario = horas_trabalhadas * valor_hora
    else:
        horas_extras = horas_trabalhadas - 40
        salario = (40 * valor_hora) + (horas_extras * valor_hora * 1.5)
    return salario