candidatos = {
    1: "Jose",
    2: "João",
    3: "Maria",
    4: "Ana"
}

votos_candidatos = {1: 0, 2: 0, 3: 0, 4: 0}
votos_nulos = 0
votos_brancos = 0

print("Digite os votos (1 a 6). Digite 0 para encerrar:")

while True:
    voto = int(input("Voto: "))
    if voto == 0:
        break
    elif voto in [1, 2, 3, 4]:
        votos_candidatos[voto] += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_brancos += 1
    else:
        print("Código de voto inválido. Tente novamente.")

total_votos = sum(votos_candidatos.values()) + votos_nulos + votos_brancos
if total_votos == 0:
    print("Nenhum voto foi registrado.")
else:
    print("\nResultado da eleição:")
    for codigo, nome in candidatos.items():
        print(f"Candidato {codigo} - {nome}: {votos_candidatos[codigo]} votos")
    print(f"Total de votos nulos: {votos_nulos}")
    print(f"Total de votos em branco: {votos_brancos}")
    print(f"Percentual de votos nulos: {(votos_nulos / total_votos) * 100:.2f}%")
    print(f"Percentual de votos em branco: {(votos_brancos / total_votos) * 100:.2f}%")