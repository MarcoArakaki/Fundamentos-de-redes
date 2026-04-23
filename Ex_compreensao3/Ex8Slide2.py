def desconto(dia, **kwargs):
    valor = kwargs.get('valor', 0)
    taxa = kwargs.get('taxa', 0)
    couvert = kwargs.get('couvert', 0)

    descontos = {
        'terça-feira': 0.10,
        'quarta-feira': 0.15,
        'quinta-feira': 0.20
    }
    desconto_aplicado = descontos.get(dia.lower(), 0)
    valor_com_desconto = valor * (1 - desconto_aplicado)

    valor_com_taxa = valor_com_desconto * (1 + taxa)

    valor_final = valor_com_taxa + couvert

    print("===== CONTA =====")
    print(f"Dia da semana: {dia}")
    print(f"Valor do consumo: R$ {valor:.2f}")
    print(f"Desconto aplicado: {desconto_aplicado*100:.0f}% → R$ {valor - valor_com_desconto:.2f}")
    print(f"Taxa de atendimento: {taxa*100:.0f}% → R$ {valor_com_desconto*taxa:.2f}")
    print(f"Couvert: R$ {couvert:.2f}")
    print(f"Valor final a pagar: R$ {valor_final:.2f}")
    print("=================")

    return valor_final

desconto('quinta-feira', valor=99.90, taxa=0.10, couvert=15)