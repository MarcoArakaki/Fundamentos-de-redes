salario = float(input("digite o salario: "))
tempo = int(input("digite o tempo trabalhado em anos: "))
if salario <= 500:
    res = salario * 1.05
elif salario >=1000 and salario < 1500:
    res = salario * 1.10
elif salario >=1500 and salario < 2000:
    res = salario * 1.10
else:
    res = salario * 1.15
add = 0
if tempo >= 1 and tempo < 4:
        add = 100
elif tempo < 1:
        add = 0
elif tempo >= 4 and tempo <=6:
        add = 200
elif tempo >= 7 and tempo <= 10:
        add = 300
else:
      add = 500
res = res + add
print (f"o preco final e = {res}")


