salarioh = float(input ("digite o salario por hora: "))
horas = int(input ("digite as horas trabalhadas: "))
salariob = salarioh * horas
inss = salariob * 0.08
sind = salariob * 0.05
ir = salariob * 0.11
print (f"o salario bruto e = {salariob}")
print (f"o desconto do imposto de renda = {ir}")
print (f"o desconto INSS = {inss}")
print (f"o desconto para o sindicato = {sind}")
salariof = salariob - inss - sind - ir
print (f"o salario liquido = {salariof}")

