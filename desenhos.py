def imprime_desenho_acerto():
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

def imprime_desenho_erro(palavra_secreta):
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

def imprime_desenho_forca(erros):
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
    