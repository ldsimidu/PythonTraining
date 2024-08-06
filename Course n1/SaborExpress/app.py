import os
#from FunctionApp import *
from list import *

def main():
    menuPrincipal()   

def menuPrincipal():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n""")

    
    print('-----|MENU|-----\n1. Sua Conta\n2. Listar Restaurantes\n3. Ativar Restaurante\n4. Sair do Aplicativo\n----------------\n')

    escolher_menu = Escolha(opcao_menu, 'Qual opção deseja escolher? (1, 2, 3 ou 4)\n-> ')
    if escolher_menu == '4':
        finalizar_app()
        
    elif escolher_menu == '2':
        restaurantesCadastrados()
    elif escolher_menu == '3':
        print('não cheguei nessa parte do curso ainda irmão')
    else:
        suaConta() 

def suaConta():

    if not lista_nomes_pessoas:
        print("Você não possui uma conta")
        desejaCadastrar()
    else:
        nome = lista_nomes_pessoas[0]
        idade = lista_idade_pessoas[0]
        telefone = lista_telefone_pessoas[0]
        email = lista_email_pessoas[0]
        cpf = lista_cpf_pessoas[0]

        print(f'\n\n---|SEUS DADOS CADASTRADOS|---\n-------------------------------\nNome: {nome}\nIdade: {idade}\nTelefone: {telefone}\nEmail: {email}\nCPF: {cpf}\n-------------------------------\n')
        voltar_menu()

def restaurantesCadastrados():

    if not lista_nomes_restaurantes:
        print('Nenhum restaurante registrado.')
    else:
        for i in range(len(lista_nomes_restaurantes)):
            print(f'\n---|RESTAURANTE {i+1}|---')
            print(f'Nome: {lista_nomes_restaurantes[i]}')
            print(f'Tipo: {lista_tipos_restaurantes[i]}')
            print(f'CNPJ: {lista_cnpj_restaurantes[i]}')
            print(f'Telefone: {lista_telefone_restaurantes[i]}')
            print(f'Email: {lista_email_restaurantes[i]}')
            print(f'Endereço: {lista_endereco_restaurantes[i]}\n')

    voltar_menu()

def desejaCadastrar():
    while True:
        deseja_cadastro = Escolha(opcao_sim_nao, 'Deseja cadastrar-se?:\nSIM(S) ou NAO(N)\n-> ')
        if deseja_cadastro == 'SIM' or deseja_cadastro == 'S':
            break
        else:
            menuPrincipal()

def inserirListasPessoa():
    usuario_cadastrado = True
    lista_nomes_pessoas.append(nome_pessoa)
    lista_idade_pessoas.append(idade_pessoa)
    lista_telefone_pessoas.append(telefone_pessoa)
    lista_email_pessoas.append(email_pessoa)
    lista_cpf_pessoas.append(cpf_pessoa)

    print(f'Seja muito Bem-Vindo(a), {nome_pessoa}! A Sabor Express fica feliz em te receber!')
    voltar_menu()

def inserirListasRestaurante():

    usuario_cadastrado = True
    lista_nomes_restaurantes.append(nome_restaurante)
    lista_tipos_restaurantes.append(tipo_restaurante)
    lista_cnpj_restaurantes.append(cnpj_restaurante)
    lista_telefone_restaurantes.append(telefone_restaurante)
    lista_email_restaurantes.append(email_restaurante)
    lista_endereco_restaurantes.append(endereco_restaurante)

    print(f'Seu Restaurante {nome_restaurante} foi cadastro com sucesso na Sabor Express!')
    voltar_menu()
    
    

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

def voltar_menu():
    voltar_menu = Escolha(opcao_voltar, 'Pressione a TECLA "B" para voltar ao Menu:\nVoltar(B)\n-> ')
    if voltar_menu == 'B': 
        limpar_tela()
        menuPrincipal() 

#FIM DAS FUNÇÕES


while True:

    menuPrincipal()
        
    while True:
        tipo_cadastro = Escolha(opcao_tipo_cadastro, '\nVocê deseja se cadastrar como:\nPESSOA(P) ou RESTAURANTE(R)?\n-> ')

        if tipo_cadastro == 'PESSOA' or tipo_cadastro == 'P':
            print('\nVocê escolheu se cadastrar como:\nPESSOA\n')
        else:
            print('\nVocê escolheu se cadastrar como:\nRESTAURANTE\n')

        continuar_cadastro = Escolha(opcao_sim_nao, 'Deseja continuar com o perfil desejado para cadastro?\nSIM(S) ou NAO(N)\n-> ')

        if continuar_cadastro == 'SIM' or continuar_cadastro == 'S':
            limpar_tela()
            while True:
                if tipo_cadastro == 'PESSOA' or tipo_cadastro == 'P':
                    nome_pessoa = input('Insira seu nome completo:\n-> ')
                    idade_pessoa = input('Insira sua idade:\n-> ')
                    telefone_pessoa = input('Insira seu Telefone:\n-> ')
                    email_pessoa = input('Insira seu email:\n-> ')
                    cpf_pessoa = input('Insira seu CPF:\n-> ')

                    print(f'\n\n---|SEUS DADOS CADASTRADOS|---\n-------------------------------\nNome: {nome_pessoa}\nIdade: {idade_pessoa}\nTelefone: {telefone_pessoa}\nEmail: {email_pessoa}\nCPF: {cpf_pessoa}\n-------------------------------\n')
                    dados_corretos_pessoa = Escolha(opcao_sim_nao, 'O seus dados estão corretos?\nSIM(S) ou NAO(N)\n-> ')

                    if dados_corretos_pessoa == 'SIM' or dados_corretos_pessoa == 'S':
                        inserirListasPessoa()
                        os.system('cls')

                else:
                    while True:
                        nome_restaurante = input('Insira o nome do seu restaurante:\n-> ')
                        tipo_restaurante = input('Insira o tipo da cozinha do seu restaurante (ex: Italiana, Japonesa, etc):\n-> ')
                        cnpj_restaurante = input('Insira o CNPJ do seu restaurante:\n-> ')
                        telefone_restaurante = input('Insira o Telefone de Contato do seu Restaurante:\n-> ')
                        email_restaurante = input('Insira o Email de Contato do seu Restaurante:\n-> ')

                        print(f'\n\n---|SEUS DADOS CADASTRADOS|---\n-------------------------------\nRazão Social: {nome_restaurante}\nCozinha: {tipo_restaurante}\nCNPJ: {cnpj_restaurante}\nTelefone: {telefone_restaurante}\nEmail: {email_restaurante}\n-------------------------------\n')
                        
                        dados_corretos_restaurante = Escolha(opcao_sim_nao, 'Os dados do seu Restaurante acima estão corretos?\nSIM(S) ou NAO(N)\n\n-> ')

                        if dados_corretos_restaurante == 'SIM' or dados_corretos_restaurante == 'S':
                            print('Insira o endereço completo do seu restaurante:\n')
                            while True:
                                estado_restaurante = input('Insira o ESTADO do seu Restaurante:\n-> ')
                                cidade_restaurante = input('Insira a CIDADE do seu Restaurante:\n-> ')
                                bairro_restaurante = input('Insira o BAIRRO do seu Restaurante:\n-> ')
                                rua_restaurante = input('Insira a RUA do seu Restaurante:\n-> ')
                                numero_restaurante = input('Insira o NÚMERO do seu Restaurante:\n-> ')

                                print(f'\n---|DADOS DO ENDEREÇO|---\n-------------------------------\n\nSeu Restaurante pertence a: {estado_restaurante}, {cidade_restaurante}, {bairro_restaurante}, {rua_restaurante}, {numero_restaurante}.\n\n-------------------------------\n\n')

                                dados_corretos_endereco_restaurante = Escolha(opcao_sim_nao, 'Os dados do endereço acima estão corretos?\nSIM(S) ou NAO(N)\n\n-> ')

                                if dados_corretos_endereco_restaurante == 'SIM' or dados_corretos_endereco_restaurante == 'S':

                                    endereco_restaurante = (f'{estado_restaurante}, {cidade_restaurante}, {bairro_restaurante}, {rua_restaurante}, {numero_restaurante}')

                                    print(f'\n\n---|SEUS DADOS CADASTRADOS|---\n-------------------------------\nRazão Social: {nome_restaurante}\nCozinha: {tipo_restaurante}\nCNPJ: {cnpj_restaurante}\nTelefone: {telefone_restaurante}\nEmail: {email_restaurante}\nEndereço Completo: {endereco_restaurante}\n-------------------------------\n')

                                    inserirListasRestaurante()
                                    

