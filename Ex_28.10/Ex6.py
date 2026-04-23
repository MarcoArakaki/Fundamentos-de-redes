class Aluno:
    def __init__(self, nome, RA, email, curso, turma):
        self.nome = nome
        self.RA = RA
        self.email = email
        self.curso = curso
        self.turma = turma

    def cadastrar_aluno(aluno):
        with open("alunos.txt","a") as arquivo:
            arquivo.write(f"{aluno.nome}, {aluno.RA}, {aluno.email}, {aluno.curso}, {aluno.turma} \n")
        print("cadastrado com sucesso!")

    def listar_alunos():
        try:
            with open("alunos.txt", "r") as arquivo:
                alunos = arquivo.readlines()
                if alunos:
                    print("Alunos cadastrados:")
                    for aluno in alunos:
                        nome, ra, email, curso, turma = aluno.strip().split(";")
                        print(f"Nome: {nome}, RA: {ra}, Email: {email}, Curso: {curso}, Turma: {turma}")
                else:
                    print("Nenhum aluno cadastrado.")
        except FileNotFoundError:
            print("Arquivo não encontrado. Nenhum aluno cadastrado.")       

    def remover_aluno(ra):
        try:
            with open("alunos.txt", "r") as arquivo:
                alunos = arquivo.readlines()

            alunos_restantes = [aluno for aluno in alunos if aluno.split(";")[1] != ra]

            if len(alunos) > len(alunos_restantes):
                with open("alunos.txt", "w") as arquivo:
                    arquivo.writelines(alunos_restantes)
                print(f"Aluno com RA {ra} removido com sucesso.")
            else:
                print(f"Aluno com RA {ra} não encontrado.")
        except FileNotFoundError:
            print("Arquivo não encontrado. Nenhum aluno cadastrado.")