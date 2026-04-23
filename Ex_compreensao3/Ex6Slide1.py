def tabela_precos():
    preco_unitario = 1.99
    print("Tabela de preços - Loja do R$ 1,99")
    print("-" * 35)
    for qtd in range(1, 51):
        total = qtd * preco_unitario
        print(f"{qtd:2} - R$ {total:6.2f}")

tabela_precos()
