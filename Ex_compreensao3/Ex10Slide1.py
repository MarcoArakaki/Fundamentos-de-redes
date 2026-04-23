def simular_financiamento():
    valor_veiculo = float(input("Informe o valor do veículo: R$ "))
    entrada = float(input("Informe o valor da entrada: R$ "))
    taxa_juros = float(input("Informe a taxa de juros ao mês (em %): "))
    parcelas = int(input("Informe a quantidade de parcelas: "))

    valor_financiado = valor_veiculo - entrada
    i = taxa_juros / 100 

    if i == 0:
        valor_parcela = valor_financiado / parcelas
    else:
        valor_parcela = valor_financiado * (i * (1 + i)**parcelas) / ((1 + i)**parcelas - 1)

    total_pago = valor_parcela * parcelas + entrada
    juros_pago = total_pago - valor_veiculo

    print("\n===== SIMULAÇÃO DE FINANCIAMENTO =====")
    print(f"Valor do veículo: R$ {valor_veiculo:.2f}")
    print(f"Entrada: R$ {entrada:.2f}")
    print(f"Valor financiado: R$ {valor_financiado:.2f}")
    print(f"Quantidade de parcelas: {parcelas}")
    print(f"Valor da parcela: R$ {valor_parcela:.2f}")
    print(f"Total pago: R$ {total_pago:.2f}")
    print(f"Juros pagos: R$ {juros_pago:.2f}")
    print("======================================")

simular_financiamento()