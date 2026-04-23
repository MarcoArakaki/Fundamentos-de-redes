def armazenar_dados(**kwargs):
    dados = dict(kwargs)
    
    print("===== DADOS DA PESSOA =====")
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")
    print("============================")

armazenar_dados(nome="Marco", idade=30, cidade="São Paulo", profissao="Engenheiro")