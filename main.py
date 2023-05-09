import advinhacao
import advinhacao_2

print("********************************")
print("Bem vindo no jogo de adivinhação")
print("********************************")

formato_escolher_jogo = False

while formato_escolher_jogo != True:
    print("(1) Advinhação (2) Advinhação 2")
    jogo = input("Defina o jogo:")

    try:
        if int(jogo) == 1:
            advinhacao.jogar()
        elif int(jogo) == 2:
            advinhacao_2.jogar()
        else:
            print("Digite um número entre 1 e 2")
    except:
        pass