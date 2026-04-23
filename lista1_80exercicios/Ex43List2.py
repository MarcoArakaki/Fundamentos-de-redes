nome = input("Atleta: ")

notas = []
for i in range(7):
    nota = float(input(f"Nota {i+1}: "))
    notas.append(nota)

melhor_nota = max(notas)
pior_nota = min(notas)

notas.remove(melhor_nota)
notas.remove(pior_nota)

media = sum(notas) / len(notas)

print("\nResultado final:")
print(f"Atleta: {nome}")
print(f"Melhor nota: {melhor_nota}")
print(f"Pior nota: {pior_nota}")
print(f"Média: {media:.2f}")