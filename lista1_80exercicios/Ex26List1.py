idade = int(input ("digite a idade: "))
tempo = int(input ("digite o tempo de servico: "))
if idade >=65:
    print ("pode se apostentar")
elif tempo >=30:
    print ("pode se aposentar")
elif idade >=60 and tempo >=25:
    print ("pode se aposentar")
else:
    print ("nao pode se aposentar")