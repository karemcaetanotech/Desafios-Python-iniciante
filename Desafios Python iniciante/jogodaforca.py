import random

def jogo_da_forca():
    palavras = ['python', 'desenvolvimento', 'tecnologia', 'qualidade']
    palavra = random.choice(palavras).lower()
    letras_corretas = []
    tentativas = 6

    print("Bem-vindo ao Jogo da Forca!")
    while tentativas > 0:
        for letra in palavra:
            if letra in letras_corretas:
                print(letra, end=" ")
            else:
                print("_", end=" ")
        print()

        tentativa = input("Adivinhe uma letra: ").lower()
        if tentativa in palavra:
            letras_corretas.append(tentativa)
        else:
            tentativas -= 1
            print(f"Letra incorreta! Você tem {tentativas} tentativas restantes.")

        if set(letras_corretas) == set(palavra):
            print("Parabéns, você acertou a palavra!")
            break
    else:
        print(f"Você perdeu! A palavra era {palavra}.")

jogo_da_forca()
