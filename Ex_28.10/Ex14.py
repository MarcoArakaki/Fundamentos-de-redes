def cadastrar_produto(nome_produto, preco_produto):
    return f"Produto '{nome_produto}' cadastrado com sucesso! Preço: R$ {preco_produto:.2f}"
try:
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = float(input("Digite o preço do produto: R$ "))
    
    # Cadastrando o produto
    mensagem = cadastrar_produto(nome_produto, preco_produto)
    print(mensagem)
    
except ValueError:
    print("Preço inválido. Digite apenas números para o valor do produto.")