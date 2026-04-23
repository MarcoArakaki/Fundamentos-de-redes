quota_base = int(input("Quota: "))
num_meses = int(input("Meses: "))

quota_atual = quota_base

for i in range(num_meses):
    consumo = int(input("Consumo: "))
    sobra = quota_atual - consumo
    quota_atual = quota_base + sobra

print(quota_atual)