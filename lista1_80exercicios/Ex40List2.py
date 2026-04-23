def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro: Divisão por zero não é permitida."
    return x / y

def exibir_menu():
    print("\n--- Menu de Calculadora ---")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Saída")
    print("--------------------------")

def main():
    while True:
        exibir_menu()
        escolha = input("Escolha uma operação (1-5): ")

        if escolha == '5':
            print("Programa encerrado.")
            break
        elif escolha in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                if escolha == '1':
                    resultado = adicionar(num1, num2)
                    print(f"Resultado: {resultado}")
                elif escolha == '2':
                    resultado = subtrair(num1, num2)
                    print(f"Resultado: {resultado}")
                elif escolha == '3':
                    resultado = multiplicar(num1, num2)
                    print(f"Resultado: {resultado}")
                elif escolha == '4':
                    resultado = dividir(num1, num2)
                    print(f"Resultado: {resultado}")
            except ValueError:
                print("Entrada inválida. Por favor, digite números válidos.")
        else:
            print("Opção inválida. Por favor, escolha um número entre 1 e 5.")

if __name__ == "__main__":
    main()