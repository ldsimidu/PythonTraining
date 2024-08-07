import os
from list import *
from app import usuario_cadastrado, Escolha

def main():
    menuPrincipal()   

'''def Finalizar_app():
    os.system('cls')
    print('Finalizando o app')'''

def finalizar_app():
    os.system('cls')
    # os.system('clear') 
    print('Finalizando o app')

def menuPrincipal():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n""")

    print('''
░█▀▀█ ░█▀▀▀ ░█▀▄▀█ 　 ░█──░█ ▀█▀ ░█▄─░█ ░█▀▀▄ ░█▀▀▀█ 
░█▀▀▄ ░█▀▀▀ ░█░█░█ 　 ─░█░█─ ░█─ ░█░█░█ ░█─░█ ░█──░█ 
░█▄▄█ ░█▄▄▄ ░█──░█ 　 ──▀▄▀─ ▄█▄ ░█──▀█ ░█▄▄▀ ░█▄▄▄█
      \n''')

    while True:
        

        
            print('''
    ▒█▀▄▀█ ▒█▀▀▀ ▒█▄░▒█ ▒█░▒█ 
    ▒█▒█▒█ ▒█▀▀▀ ▒█▒█▒█ ▒█░▒█ 
    ▒█░░▒█ ▒█▄▄▄ ▒█░░▀█ ░▀▄▄▀
            \n\n''')

            print('1. Sua Conta\n2. Listar Restaurantes\n3. Ativar Restaurante\n4. Sair do Aplicativo\n\n')

            escolher_menu = Escolha(opcao_menu, 'Qual opção deseja escolher? (1, 2, 3 ou 4)\n-> ')
            if escolher_menu == '1':
                suaConta()
            elif escolher_menu == '2':
                print('não cheguei nessa parte do curso ainda irmão')
            elif escolher_menu == '3':
                print('não cheguei nessa parte do curso ainda irmão')
            else:
                finalizar_app()
   
def suaConta():

    while not lista_nomes_pessoas:
        print("Você não possui uma conta")
        break
    else:
        nome = lista_nomes_pessoas[0]
        idade = lista_idade_pessoas[0]
        telefone = lista_telefone_pessoas[0]
        email = lista_email_pessoas[0]
        cpf = lista_cpf_pessoas[0]

        print(f"Nome: {nome}")
        print(f"Idade: {idade}")
        print(f"Telefone: {telefone}")
        print(f"Email: {email}")
        print(f"CPF: {cpf}")






 