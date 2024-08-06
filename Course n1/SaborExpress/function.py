import os
from list import *
from app import usuario_cadastrado

def main():
    menuPrincipal()   

def Escolha(lista_opcoes, msg):
    escolha = input(msg).upper()
    while escolha not in lista_opcoes:
        print('\nEscolha uma opção válida\n')
        escolha = input(msg).upper()
    return escolha

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
        

        if cadastro_sim_nao == 'NAO' or cadastro_sim_nao == 'N':
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
        else:
            break
   

def suaConta():
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


    dados_pessoa_0 = [
        nome,
        idade,
        telefone,
        email,
        cpf
    ]

    print(dados_pessoa_0)





 