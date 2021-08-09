import random

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

def jogar():
    msg_abertura()

    palavra_secreta = carrega_palavra_secreta()
 
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    while(not enforcou and not acertou):
        print(f"Erros {erros} de 6")        
        chute = input("Digite uma Letra.: ")
        chute = chute.strip().upper() #retirando os espaços e deixando a letra maiuscula

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if letra == chute:
                    letras_acertadas[index] = letra
                else:
                    print(f"{letra} {index}")
                
                index += 1     
        else:
            erros += 1

        print(letras_acertadas)
        enforcou = erros == 6         
        acertou = not '_' in letras_acertadas 
    
    print("="*40)
    if acertou:
        print("Parabéns... Você ACERTOU a Palavra... 0/")
    elif enforcou:
        print("Que Pena.. Você foi ENFORCADO...")        
        print("Atingiu os 6 erros...") 
        print(f"A Palavra SECRETA era.: {palavra_secreta}")
    print("="*40)       

if (__name__ == "__main__"):
    jogar()
        