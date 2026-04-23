class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def mostrar_nome(self):
        print(f"Nome: {self.nome}")

    def alterar_idade(self, nova_idade):
        self.idade = nova_idade
        print(f"Idade alterada para: {self.idade}")

    def imprimir_endereco(self):
        print(f"Endereço: {self.endereco}")


pessoa1 = Pessoa("Marco", 25, "Campo Grande Insted")
pessoa1.mostrar_nome()        
pessoa1.alterar_idade(18)
pessoa1.imprimir_endereco()