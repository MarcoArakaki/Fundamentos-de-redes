with open("crescente.txt", "w") as arquivo:
    for i in range (1,101):
        arquivo.write(f"{i};")

with open("crescente.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print (conteudo)
