num = int(input("Digite quantos numeros impares em sequencia comecando do 1 deseja: "))
print(f"Os {num} primeiros números impares sao:")
for impar in range(1, num * 2, 2):
  print(impar)
