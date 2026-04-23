import random

def sorteiaAluno(qtd_alunos):
    alunos = []
    for i in range(qtd_alunos):
        nome = input(f"Digite o nome do {i+1}º aluno: ")
        alunos.append(nome)


    primeiro = random.choice(alunos)
    print(f"O primeiro aluno(a) a apresentar será: {primeiro}")

sorteiaAluno(6)