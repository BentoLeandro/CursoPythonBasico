import os
import forca
import adivinhacao

def escolher_jogo():
    continuar_jogando = True
    escolher_jogo = True
    while continuar_jogando:
        os.system('cls') #limpa o terminal
        
        if escolher_jogo:
            print("**********************************")
            print("****** Escolha o seu Jogo! *******")
            print("**********************************")

            print("(1) Forca (2) Adivinhação")
            jogo = int(input("Qual o Jogo deseja jogar?.: "))

        if (jogo == 1):
            print("Jogando Forca...")
            forca.jogar()
        elif (jogo == 2):
            print("Jogando Adivinhação...")
            adivinhacao.jogar()

        opcao_valida = False
        while not opcao_valida:
            print("****************************************")
            print("Deseja Continuar Jogando ?")    
            print("Opções...")
            print("S - Jogar o mesmo Jogo") 
            print("E - Escolher outro Jogo")
            print("N - Sair")
            opcao = input("Digite o que deseja fazer.: ")
            opcao = opcao.upper()
            print("****************************************")    

            opcao_valida = True
            if opcao == 'N':
                continuar_jogando = False
            elif opcao == 'E':
                escolher_jogo = True
            elif opcao == 'S':
                escolher_jogo = False
            else:
                opcao_valida = False
                os.system("cls")
                print(f"Opção.: {opcao} é invalida!")
                print("Digite uma das opções.: S - E - N")    



if (__name__ == "__main__"):
    escolher_jogo()        
