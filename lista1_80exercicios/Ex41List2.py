limite = 100
soma_dos_quadrados = sum([i**2 for i in range(1, limite + 1)])

quadrado_da_soma = sum(range(1, limite + 1))**2

diferenca = quadrado_da_soma - soma_dos_quadrados

print(f"A soma dos quadrados dos primeiros {limite} números naturais é: {soma_dos_quadrados}")
print(f"O quadrado da soma dos primeiros {limite} números naturais é: {quadrado_da_soma}")
print(f"A diferença é: {diferenca}")