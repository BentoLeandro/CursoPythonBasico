import random

def jogar():
    print("**********************************")
    print("Bem-vindo ao Jogo de Adivinhação..")
    print("**********************************")

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

    #while (numero_tentativas > 0):
    for rodada in range(1, numero_tentativas+1):
        print(f"Tentativa.: {rodada} de {numero_tentativas}")
        print("**********************************")
        chute = int(input("Digite o seu número entre(1 e 100).: "))    

        if (chute < 1 or chute > 100):
            print("O número precisa estar entre 1 e 100...")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print("**** Parabéns... Você acertou o Número... 0/ ****")
            print(f"**** Você Finalizou o jogo com {pontos} pontos...")
            break
        else:
            if (maior):
                print(f"Errou... :( Seu Chute {chute} foi MAIOR que o número secreto...")
            elif (menor):
                print(f"Errou... :( Seu Chute {chute} foi MENOR que o número secreto... ")

            pontos_perdidos = abs(numero_secreto - chute) 
            pontos = pontos - pontos_perdidos    

        print("**********************************")
        #numero_tentativas -= 1 
    else:
        print("Que pena acabaram suas Tentativas...")
        print(f"O Número secreto era.: {numero_secreto}")
        print(f"Sua pontuação Final foi.: {pontos}")               
        
    print("**********************************")
    print("********** FIM do Jogo************")

if (__name__ == '__main__'):
    jogar()    