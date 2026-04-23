def abrir_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as file:
            print(f"Arquivo '{nome_arquivo}' aberto com sucesso!")
            conteudo = file.read()
            print(conteudo)
    except FileNotFoundError:
        print("Arquivo não encontrado.")