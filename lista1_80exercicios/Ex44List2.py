total_pessoas = 25

idades = []
sexos = []
alturas = []
pesos = []
imcs = []

for i in range(total_pessoas):
    print(f"\nPessoa {i+1}:")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").strip().upper()
    while sexo not in ['M', 'F']:
        sexo = input("Sexo inválido. Digite 'M' para masculino ou 'F' para feminino: ").strip().upper()
    altura = float(input("Altura (m): "))
    peso = float(input("Peso (kg): "))

    idades.append(idade)
    sexos.append(sexo)
    alturas.append(altura)
    pesos.append(peso)

    imc = peso / (altura ** 2)
    imcs.append(imc)

idade_mais_velha = max(idades)
altura_mais_alta = max(alturas)
maior_peso = max(pesos)
media_altura = sum(alturas) / total_pessoas
media_imc = sum(imcs) / total_pessoas
porcentagem_masculino = (sexos.count('M') / total_pessoas) * 100
porcentagem_feminino = (sexos.count('F') / total_pessoas) * 100

print("\nResultados da Academia BemMaisFort:")
print(f"Idade da pessoa mais velha: {idade_mais_velha} anos")
print(f"Altura da pessoa mais alta: {altura_mais_alta:.2f} m")
print(f"Maior peso: {maior_peso:.2f} kg")
print(f"Média de altura: {media_altura:.2f} m")
print(f"Média de IMC: {media_imc:.2f}")
print(f"Porcentagem de Sexo Masculino: {porcentagem_masculino:.2f}%")
print(f"Porcentagem de Sexo Feminino: {porcentagem_feminino:.2f}%")