import os
from lists import *
from app import menuPrincipal

def verificar_numero(msg):
    while True:
        numero = input(msg)
        if not numero.isnumeric():
            print('O valor inserido não é um número.')
        else:
            return int(numero)
    
def Escolha(lista_opcoes, msg):
    escolha = input(msg).upper()
    while escolha not in lista_opcoes:
        print('\nEscolha uma opção válida\n')
        escolha = input(msg).upper()
    return escolha

def finalizar_app():
    os.system('cls')
    # os.system('clear') 
    print('Finalizando o app')
    exit()

def limpar_tela():
    os.system('cls')

def voltar_menu(lista_nomes_restaurantes):
    voltar_menu = Escolha(opcao_voltar, 'Pressione a TECLA "B" para voltar ao Menu:\nVoltar(B)\n-> ')
    if voltar_menu == 'B': 
        limpar_tela()
        menuPrincipal(lista_nomes_restaurantes)