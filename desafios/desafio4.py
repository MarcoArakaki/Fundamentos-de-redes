a = float(input("a: "))
n = int(input("n: "))
r = float(input("r: "))

pa = [a + i*r for i in range(n)]

print(pa)

if n >= 5:
    print(f"O quinto termo é: {pa[4]}")

termo_central = (pa[0] + pa[-1]) / 2
print(f"O termo central é: {termo_central}")

total_cabos = sum(pa)
print(f"Total: {total_cabos} metros")