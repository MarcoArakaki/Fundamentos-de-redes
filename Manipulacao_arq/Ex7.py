try:
    idade = int(input("Por favor, insira sua idade: "))
    print(f"Sua idade é {idade} anos.")
except ValueError:
    print("Por favor, insira uma idade válida.")