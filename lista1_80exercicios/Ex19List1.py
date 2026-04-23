trabalho = float(input("Digite a nota do Trabalho de Laboratrio: "))
avaliacao = float(input("Digite a nota da Avaliação Semestral: "))
exame = float(input("Digite a nota do Exame Final: "))
if (0 < trabalho > 10):
    print("Erro: a nota do Trabalho deve estar entre 0 e 10.")
elif (0 < avaliacao > 10):
    print("Erro: a nota da Avaliação deve estar entre 0 e 10.")
elif (0 < exame > 10):
    print("Erro: a nota do Exame deve estar entre 0 e 10.")
else:
    media = (trabalho*2 + avaliacao*3 + exame*5) / (2+3+5)

    print(f"A Media final e : {media}")
    if 0 <= media <= 2.9:
        print("REPROVADO")
    elif 3 <= media <= 5.9:
        print("RECUPERAÇÃO")
    else:
        print("APROVADO")