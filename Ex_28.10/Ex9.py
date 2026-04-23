def realizar_saque(saldo, valor_saque):
    if valor_saque > saldo:
        raise ValueError("Saldo insuficiente para realizar o saque.")
    else:
        saldo -= valor_saque
        return saldo