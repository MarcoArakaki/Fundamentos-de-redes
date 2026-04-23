with open("decrescente.txt", "w") as arquivo:
    for i in range (100, 0, -1):
        arquivo.write(f"{i};")

with open("decrescente.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print (conteudo)