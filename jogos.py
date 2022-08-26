import forca
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("******Escolha seu jogo!******")
    print("*********************************")

    print("(1) forca (2) Advinhação ")

    jogo = int(input("Qual jogos?"))

    if(jogo == 1):
        print("jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("jogando advinhação")
        adivinhacao.jogar()
if(__name__ == "__main__"):
    escolhe_jogo()