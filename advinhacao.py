import random

def jogar():
    print("********************************")
    print("Bem vindo no jogo de adivinhação")
    print("********************************")

    min_numero_secreto = 1
    max_numero_secreto = 100
    contador = 0
    pontos = 100
    numero_secreto = round(random.randrange(min_numero_secreto,max_numero_secreto))
    chute_formato_correto = False
    nivel_formato_correto = False

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


    while total_tentativas > contador:
        print(f"Rodada: {contador + 1}/{total_tentativas}")
        while chute_formato_correto != True:
            chute_str = input("Digite o seu número: ")
            
            try:
                chute_int = int(chute_str) 

                if(chute_int < min_numero_secreto or chute_int > max_numero_secreto):
                    print("Você deve digitar um número entre {} e {}".format(min_numero_secreto,max_numero_secreto))
                    continue

                acertou = numero_secreto == chute_int
                maior = chute_int > numero_secreto
                menor = chute_int < numero_secreto
                chute_formato_correto = True
                contador += 1
            except:
                pass

        chute_formato_correto = False

        if (acertou):
            print("Você acertou e sua pontuação é {}".format(pontos))
            break
        elif(maior):
            pontos =- abs(numero_secreto - chute_int)
            print("Você errou! O seu chute foi maior do que o número secreto e digitou: {}".format(chute_int))
        elif(menor):
            pontos =- abs(numero_secreto - chute_int)
            print("Você errou! O seu chute foi menor do que o número secreto e digitou: {}".format(chute_int))

    print("O jogo foi encerrado")


if(__name__ == "__main__"):
    jogar()