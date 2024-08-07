import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 10)
    tentativas = 0
    acertou = False

    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número entre 1 e 10.")

    while not acertou:
        palpite = int(input("Digite o seu palpite: "))
        tentativas += 1

        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
            acertou = True
        elif palpite < numero_secreto:
            print("Muito baixo! Tente novamente.")
        else:
            print("Muito alto! Tente novamente.")

if __name__ == "__main__":
    jogo_adivinhacao()