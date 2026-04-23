horas = float(input ("digite o numero de horas trabalhadas: "))
salariob = horas * 40.50
if salariob > 2500:
    salariof = salariob * 0.89
    print (f"salario final = {salariof}")
else:
    print (f"salario final = {salariob}")