import random
import os
import desenhos

def msg_abertura():
    print("**********************************")
    print("***Bem-vindo ao Jogo da Forca..***")
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
    desenhos.imprime_desenho_acerto()
    print("="*40)


def imprime_msg_erro(palavra_secreta):
    print("="*33)    
    desenhos.imprime_desenho_erro(palavra_secreta)
    print("="*33)


def jogar():
    os.system('cls')
    palavra_secreta = carrega_palavra_secreta()
 
    letras_acertadas = ["_" for letra in palavra_secreta]    

    enforcou = False
    acertou = False
    erros = 0
    
    while(not enforcou and not acertou):
        msg_abertura()
        desenhos.imprime_desenho_forca(erros)
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
        