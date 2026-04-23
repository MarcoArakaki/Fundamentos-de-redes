x = int(input("Digite a base (x): "))
y = int(input("Digite o expoente (y): "))
resultado = 1
for i in range(y):
    resultado *= x
print(f"{x}^{y} = {resultado}")