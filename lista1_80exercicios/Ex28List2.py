atual = int(input("digite o ano atual: "))

salario = 4000 
aumento = 0.015  
for ano in range(2020, atual + 1):
    salario += salario * aumento
    aumento *= 2 

print(f"Salário atual em {atual}: R$ {salario}")
