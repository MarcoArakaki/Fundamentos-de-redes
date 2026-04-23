def calcular_resistores_paralelo():

    while True:
        try:
            r1_str = input("Insira o valor de R1 (em Ohms) ou 0 para sair: ")
            r1 = float(r1_str)

            if r1 == 0:
                print("Programa finalizado.")
                break

            r2_str = input("Insira o valor de R2 (em Ohms) ou 0 para sair: ")
            r2 = float(r2_str)

            if r2 == 0:
                print("Programa finalizado.")
                break

            if r1 < 0 or r2 < 0:
                print("Os valores de resistência devem ser positivos. Tente novamente.")
                continue
            elif (r1 + r2) == 0:
                print("A soma das resistências não pode ser zero para cálculo em paralelo. Tente novamente.")
                continue
            else:
                r_equivalente = (r1 * r2) / (r1 + r2)
                print(f"A resistência equivalente (R_eq) de {r1} Ohms e {r2} Ohms em paralelo é: {r_equivalente:.2f} Ohms\n")

        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido para a resistência.\n")

calcular_resistores_paralelo()