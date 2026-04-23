def salario(horasT, valor):
    if horasT <= 40:
        salario = horasT * valor
    else:
        salariob = 40 * valor

        hora_extra = horasT - 40
        sal_extra = hora_extra * (valor * 1.5)
        salario = salariob + sal_extra
    return salario

print(salario(35, 20))