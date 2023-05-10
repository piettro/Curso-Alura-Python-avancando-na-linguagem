import random

def jogar():
    print("********************************")
    print("Bem vindo no jogo de adivinhação 2")
    print("********************************")

    ##Selecionando a palavra secreta
    arquivo = open("palavras.txt","r")
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip())
    arquivo.close()

    ##Variaveis iniciais
    palavra_secreta = palavras[random.randrange(0,len(palavras))].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    letras_erradas = []
    enforcou = False
    acertou = False
    cont = 0
    tentativas = 3

    ##Jogo
    while (not enforcou and not acertou and cont < tentativas):
        print(f"Você ainda tem {tentativas - cont} de {tentativas} tentativas")
        chute = input("Qual letra?")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index = index + 1
        else:
            cont += 1

        if ("_" not in letras_acertadas):
            print("Fim do jogo, você ganhou!!")
            break

        print(letras_acertadas)

    if (cont == tentativas):
        print(f"Fim do jogo, você perdeu. A palavra secreta era {palavra_secreta.lower()}")

if (__name__ == "__main__"):
    jogar()
