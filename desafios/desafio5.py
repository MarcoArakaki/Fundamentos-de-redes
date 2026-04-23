vermelho = int(input("Digite o valor (Vermelho): "))
amarelo = int(input("Digite o valor (Amarelo): "))
verde = int(input("Digite o valor (Verde): "))

status = [vermelho, amarelo, verde]
ligadas = sum(status)

if ligadas == 0:
    print("Semáforo desligado!!")
    print(f"Status: {vermelho} {amarelo} {verde}")
elif ligadas == 1:
    if vermelho == 1:
        cor = "Vermelho"
    elif amarelo == 1:
        cor = "Amarelo"
    else:
        cor = "Verde"
    print(f"{cor} ON")
    print(f"Status: {vermelho} {amarelo} {verde}")
else:
    print("Entrada inválida!")