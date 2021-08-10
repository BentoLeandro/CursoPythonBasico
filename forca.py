import random
import os

def msg_abertura():
    print("**********************************")
    print("***Bem vindo ao Jogo da Forca..***")
    print("**********************************")

def carrega_palavra_secreta():
    palavras = []
    with open("palavras.txt", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
    

    numero = random.randrange(0, len(palavras))
    return palavras[numero].upper()

def busca_chute():
    chute = input("Digite uma Letra.: ")
    chute = chute.strip().upper() #retirando os espaços e deixando a letra maiuscula    
    return chute

def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if letra == chute:
            letras_acertadas[index] = letra
        #else:
            #print(f"{letra} {index}")
        
        index += 1    
        
def imprime_msg_acerto(palavra_secreta):
    print("="*40)
    print("Parabéns... Você ACERTOU a Palavra... 0/")
    print(f"Palavra secreta.: {palavra_secreta}")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    print("="*40)


def imprime_msg_erro(palavra_secreta):
    print("="*33)    
    print("    _______________       ")
    print("   /               \      ")
    print("  /                 \     ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /  ")
    print(" |   XXXX     XXXX   |/   ")
    print(" |   XXX       XXX   |   Que Pena.. Você foi ENFORCADO...  ")
    print(" |                   |   Atingiu os 7 erros... ")
    print(f" \__      XXX      __/   A Palavra SECRETA era.: {palavra_secreta} ")
    print("   |\     XXX     /|      ")
    print("   | |           | |      ")
    print("   | I I I I I I I |      ")
    print("   |  I I I I I I  |      ")
    print("   \_             _/      ")
    print("     \_         _/        ")
    print("       \_______/          ")
    print("="*33)

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 0):
        print(" | ")
        print(" | ")
        print(" | ")
        print(" | ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()    

def jogar():
    os.system('cls')
    palavra_secreta = carrega_palavra_secreta()
 
    letras_acertadas = ["_" for letra in palavra_secreta]    

    enforcou = False
    acertou = False
    erros = 0
    
    while(not enforcou and not acertou):
        msg_abertura()
        desenha_forca(erros)
        print(f"Erros {erros} de 7")     
        print(letras_acertadas)   
        chute = busca_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)     
        else:
            erros += 1            
        
        enforcou = erros == 7         
        acertou = not '_' in letras_acertadas 
        os.system('cls')
        
    if acertou:
        imprime_msg_acerto(palavra_secreta)        
    elif enforcou:
        imprime_msg_erro(palavra_secreta)               

if (__name__ == "__main__"):
    jogar()
        