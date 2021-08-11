import random
import os

def msg_abertura():
    print("**********************************")
    print("Bem-vindo ao Jogo de Adivinhação..")
    print("**********************************")
    print()

def msg_tentativas(lista, rodada, numero_tentativas):
    print(lista)
    print(f"Tentativa.: {rodada} de {numero_tentativas}")
    print("**********************************")

def verifica_chute(chute, numero_secreto, pontos):    
    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print("**** Parabéns... Você acertou o Número... 0/ ****")
        print(f"**** Você Finalizou o jogo com {pontos} pontos...")
        return acertou
    else:
        if (maior):
            print(f"Errou... :( Seu Chute {chute} foi MAIOR que o número secreto...")
        elif (menor):
            print(f"Errou... :( Seu Chute {chute} foi MENOR que o número secreto... ")
                
def jogar():
    os.system("cls")
    msg_abertura()

    numero_secreto = random.randrange(1, 101) #round(random.random() * 100)
    numero_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade ??")
    print("(1)Fácil (2)Médio (3)Difícil")

    nivel = int(input("Digite o Nível.: "))

    if (nivel == 1):
        numero_tentativas = 20
    elif (nivel == 2):
        numero_tentativas = 10
    else:
        numero_tentativas = 5        

    lista_tentativas = ['_' for qtd in range(0, numero_tentativas)]
    
    os.system("cls")
    chute = 0
    for rodada in range(1, numero_tentativas+1):        
        msg_abertura()
        msg_tentativas(lista_tentativas, rodada, numero_tentativas)
        if chute > 0:
            acertou = verifica_chute(chute, numero_secreto, pontos)
            
            if acertou:
                break # sai do loop quando acerta o numero

        num_valido = False        
        while not num_valido:      
            try:  
                chute = int(input("Digite o seu número entre(1 e 100).: "))
                num_valido = (chute >= 1 and chute <= 100)
            except:                                                                       
                pass

            if not num_valido:            
                os.system("cls")
                msg_abertura()
                msg_tentativas(lista_tentativas, rodada, numero_tentativas)
                print("ATENÇÃO...O número precisa estar entre 1 e 100...")
            
        lista_tentativas[rodada-1] = chute   
                
        pontos_perdidos = abs(numero_secreto - chute) 
        pontos = pontos - pontos_perdidos

        print("**********************************")
        os.system("cls")         
    else:
        print("Que pena acabaram suas Tentativas...")
        print(f"O Número secreto era.: {numero_secreto}")
        #print(f"Sua pontuação Final foi.: {pontos}")               

    print()    
    print("**********************************")
    print("********** FIM do Jogo************")

if (__name__ == '__main__'):
    jogar()    