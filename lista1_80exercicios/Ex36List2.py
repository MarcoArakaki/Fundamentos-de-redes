def soma_impares_intervalo():
    """
    Soma os números ímpares dentro de um intervalo especificado pelo utilizador.
    """
    try:
        valor_inicial = int(input("Digite o valor inicial do intervalo: "))
        valor_final = int(input("Digite o valor final do intervalo: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números inteiros.")
        return

    if valor_inicial > valor_final:
        print("Intervalo de valores inválido")
        return

    soma = 0
    for numero in range(valor_inicial, valor_final + 1):
        if numero % 2 != 0:
            soma += numero

    print(f"Soma dos ímpares neste intervalo: {soma}")

soma_impares_intervalo()