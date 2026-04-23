class Livro:
    def __init__(self, nome, autor, editora, paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas

    def alterar_editora(self, nova_editora):
        self.editora = nova_editora
        print(f"Editora alterada para: {self.editora}")

    def listar_qtde_paginas(self):
        print(f"O livro '{self.nome}' possui {self.paginas} páginas.")


livro1 = Livro("Aula Python", "Thiago", "Editora Insted", 250)
livro1.listar_qtde_paginas()
livro1.alterar_editora("Editora Insted2")