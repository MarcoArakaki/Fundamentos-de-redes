S = 0
numerador = 1
for denominador in range(1, 51):
    S += numerador / denominador
    numerador += 2

print(f"O valor de S e = {S}")