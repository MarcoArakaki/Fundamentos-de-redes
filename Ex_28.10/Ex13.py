def dividir_conta(valor_conta, num_pessoas):
    if num_pessoas <= 0:
        raise ValueError("Número de pessoas inválido para divisão da conta.")
    else:
        valor_por_pessoa = valor_conta / num_pessoas
        return valor_por_pessoa