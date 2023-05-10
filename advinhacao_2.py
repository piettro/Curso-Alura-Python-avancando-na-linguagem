import random

def gerar_mensagem_inicio():
    print("********************************")
    print("Bem vindo no jogo da forca")
    print("********************************")


def gerar_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip())
    arquivo.close()

    palavra_secreta = palavras[random.randrange(0, len(palavras))].upper()
    return palavra_secreta


def jogar():
    jogando = True

    while jogando:
        gerar_mensagem_inicio()

        # Variaveis iniciais
        palavra_secreta = gerar_palavra_secreta()
        letras_acertadas = ["_" for letra in palavra_secreta]
        enforcou = False
        acertou = False
        cont = 0
        total_tentativas = 3
        jogando = True
        nivel_formato_correto = False
        continuar_formato_correto = False

        print("Qual é o nível de dificuldade? \n (1) Fácil (2) Médio (3) Difícil")

        while nivel_formato_correto != True:
            nivel = input("Defina o nível: ")

            try:
                if int(nivel) == 1:
                    total_tentativas = 20
                    nivel_formato_correto = True
                elif int(nivel) == 2:
                    total_tentativas = 10
                    nivel_formato_correto = True
                elif int(nivel) == 3:
                    total_tentativas = 5
                    nivel_formato_correto = True
                else:
                    print("Digite um número entre 1 e 3")
            except:
                pass

        # Jogo
        while (not enforcou and not acertou and cont < total_tentativas):
            print(f"Você ainda tem {total_tentativas - cont} de {total_tentativas} tentativas")
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

            if (cont == total_tentativas):
                print(
                    f"Fim do jogo, você perdeu. A palavra secreta era {palavra_secreta.lower()}")

        print(f"Você quer jogar novamente?")
        while continuar_formato_correto != True:
            continuar_jogando = input("Digite 1 para continuar e 0 para sair do jogo \n")

            try:
                if int(continuar_jogando) == 0:
                    jogando = False
                    continuar_formato_correto = True
                elif int(continuar_jogando) == 1:
                    jogando = True
                    continuar_formato_correto = True
            except:
                pass


if (__name__ == "__main__"):
    jogar()
