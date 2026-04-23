caracteres = []
vogais = ['a', 'e', 'i', 'o', 'u']
consoantes_encontradas = []
for i in range(10):
    caractere = input(f"Por favor, insira o {i+1}º caractere: ").lower()
    caracteres.append(caractere)
    if caractere not in vogais and caractere.isalpha():
        consoantes_encontradas.append(caractere)
print("\nConsoantes encontradas:")
for consoante in consoantes_encontradas:
    print(consoante)
print(f"\nTotal de consoantes lidas: {len(consoantes_encontradas)}")