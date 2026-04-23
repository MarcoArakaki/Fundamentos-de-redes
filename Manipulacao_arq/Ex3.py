lista = []

print("digite a frase que deseja adicionar(digite 0 para finalizar) :")
while True:
    frase = input("digite uma frase: ")
    
    if (frase == '0'):
        break

lista.append(frase)

with open("frases.txt", "w") as arquivo:
    for frase in lista:
        arquivo.write(frase + "\n")

