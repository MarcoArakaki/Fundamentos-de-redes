class Aluno:
    def __init__(self, nome, ra, nota1, nota2, nota3, nota4):
        self.nome = nome
        self.ra = ra
        self.notas = [nota1, nota2, nota3, nota4]

    def mostrar_situacao(self):
        media = sum(self.notas) / len(self.notas)
        if media >= 7:
            situacao = "APROVADO"
        elif 5 <= media < 7:
            situacao = "EXAME"
        else:
            situacao = "REPROVADO"
        print(f"Aluno: {self.nome} | RA: {self.ra} | Média: {media:.2f} | Situação: {situacao}")
        return situacao


aluno = Aluno("Marco", "12345", 8.0, 7.5, 6.0, 9.0)
aluno.mostrar_situacao()