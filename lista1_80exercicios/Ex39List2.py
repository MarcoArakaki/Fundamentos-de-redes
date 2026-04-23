import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")

    while True:
        try:
            chute_str = input("Insira o seu palpite: ")
            chute = int(chute_str) 
            tentativas += 1

            if chute < numero_secreto:
                print("Muito baixo! Tente um número maior.")
            elif chute > numero_secreto:
                print("Muito alto! Tente um número menor.")
            else:
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas!")
                break 
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

jogo_adivinhacao()