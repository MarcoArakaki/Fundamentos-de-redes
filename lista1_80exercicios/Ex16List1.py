salario = float(input ("digite o salario do beneficiado: "))
parcela = float(input ("digite o valor da pestacao do emprestimo: "))
teste = salario * 0.20
if parcela > teste:
    print ("emprestimo nao concedido")
else:
    print ("emprestimo concedido")