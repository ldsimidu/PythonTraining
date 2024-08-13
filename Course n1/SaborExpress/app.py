import os
#from FunctionApp import *
from lists import *
from globalFunction import *


def main():
    menuPrincipal(lista_nomes_restaurantes)   

def deseja_listar_restaurante_ou_prato():
    restaurante_ou_prato = Escolha(opcao_restaurante_prato, 'Deseja listar:\nRESTAURANTES(R) ou PRATOS(P)\n-> ')
    if restaurante_ou_prato == 'RESTAURANTE' or restaurante_ou_prato == 'R':
        restaurantesCadastrados()
        limpar_tela()
    else:
        pratos_cadastrados()
        limpar_tela()
    
def deseja_cadastrar_restaurante_prato(lista_nomes_restaurantes):
    restaurante_ou_prato = Escolha(opcao_restaurante_prato, 'Deseja Cadastrar:\nRESTAURANTES(R) ou PRATOS(P)\n-> ')
    if restaurante_ou_prato == 'RESTAURANTE' or restaurante_ou_prato == 'R':
        cadastrar_restaurantes(lista_nomes_restaurantes)
        limpar_tela()
    else:
        cadastrar_pratos_restaurantes(lista_nomes_restaurantes)
        limpar_tela()
        
def menuPrincipal(lista_nomes_restaurantes):
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n""")

    
    print('-----|MENU|-----\n1. Sua Conta\n2. Cadastrar Novo Restaurante/Prato\n3. Listar Restaurantes/Pratos\n4. Ativar Restaurante\n5. Sair do Aplicativo\n----------------\n')

    escolher_menu = Escolha(opcao_menu, 'Qual opção deseja escolher? (1, 2, 3 ou 4)\n-> ')
    if escolher_menu == '5':
        finalizar_app()
    elif escolher_menu == '2':
        deseja_cadastrar_restaurante_prato(lista_nomes_restaurantes)
    elif escolher_menu == '3':
        deseja_listar_restaurante_ou_prato()
    elif escolher_menu == '4':
        print('não cheguei nessa parte do curso ainda irmão')
    else:
        suaConta() 

def suaConta():

    if not lista_nomes_pessoas:
        print("Você não possui uma conta")
        deseja_cadastrar_conta()
    else:
        nome = lista_nomes_pessoas[0]
        idade = lista_idade_pessoas[0]
        telefone = lista_telefone_pessoas[0]
        email = lista_email_pessoas[0]
        cpf = lista_cpf_pessoas[0]

        print(f'\n\n---|SEUS DADOS CADASTRADOS|---\n-------------------------------\nNome: {nome}\nIdade: {idade}\nTelefone: {telefone}\nEmail: {email}\nCPF: {cpf}\n-------------------------------\n\n')
        editar_dados = Escolha(opcao_sim_nao, 'Deseja editar seus dados?:\nSIM(S) ou NAO(N)\n-> ')
        if editar_dados == 'SIM' or editar_dados == 'S':
            cadastrarPessoa()
        else:
            voltar_menu()

def restaurantesCadastrados():

    if not lista_nomes_restaurantes:
        limpar_tela()
        print('Nenhum restaurante registrado.')
    else:
        limpar_tela()
        for i in range(len(lista_nomes_restaurantes)):
            print(f'\n---|RESTAURANTE {i+1}|---')
            print(f'Nome: {lista_nomes_restaurantes[i]}')
            print(f'Tipo: {lista_tipos_restaurantes[i]}')
            print(f'CNPJ: {lista_cnpj_restaurantes[i]}')
            print(f'Telefone: {lista_telefone_restaurantes[i]}')
            print(f'Email: {lista_email_restaurantes[i]}')
            print(f'Endereço: {lista_endereco_restaurantes[i]}\n')

    voltar_menu(lista_nomes_restaurantes)

def deseja_cadastrar_conta():
    #while True:
    deseja_cadastro = Escolha(opcao_sim_nao, 'Deseja cadastrar-se?:\nSIM(S) ou NAO(N)\n-> ')
    if deseja_cadastro == 'SIM' or deseja_cadastro == 'S':
        '''tipo_cadastro = Escolha(opcao_tipo_cadastro, '\nVocê deseja se cadastrar uma:\nCONTA(P) ou RESTAURANTE(R)?\n-> ')

        if tipo_cadastro == 'PESSOA' or tipo_cadastro == 'P':
            print('\nVocê escolheu se cadastrar uma:\nCONTA\n')
        else:
            print('\nVocê escolheu se cadastrar um :\nRESTAURANTE\n')'''

        '''continuar_cadastro = Escolha(opcao_sim_nao, 'Deseja continuar com o perfil desejado para cadastro?\nSIM(S) ou NAO(N)\n-> ')
        if continuar_cadastro == 'SIM' or continuar_cadastro == 'S':'''
        limpar_tela()    
        while True:
            cadastrarPessoa()
            
    else:
        limpar_tela()
        menuPrincipal(lista_nomes_restaurantes)

def inserirListasPessoa(nome_pessoa, idade_pessoa, telefone_pessoa, email_pessoa, cpf_pessoa):
    usuario_cadastrado = True
    lista_nomes_pessoas.append(nome_pessoa)
    lista_idade_pessoas.append(idade_pessoa)
    lista_telefone_pessoas.append(telefone_pessoa)
    lista_email_pessoas.append(email_pessoa)
    lista_cpf_pessoas.append(cpf_pessoa)

    print(f'Seja muito Bem-Vindo(a), {nome_pessoa}! A Sabor Express fica feliz em te receber!')
    voltar_menu(lista_nomes_restaurantes)

def inserirListasRestaurante(lista_nomes_restaurantes, nome_restaurante, tipo_restaurante, cnpj_restaurante, telefone_restaurante, email_restaurante, endereco_restaurante):

    usuario_cadastrado = True
    lista_nomes_restaurantes.append(nome_restaurante)
    lista_tipos_restaurantes.append(tipo_restaurante)
    lista_cnpj_restaurantes.append(cnpj_restaurante)
    lista_telefone_restaurantes.append(telefone_restaurante)
    lista_email_restaurantes.append(email_restaurante)
    lista_endereco_restaurantes.append(endereco_restaurante)

    print(f'Seu Restaurante {nome_restaurante} foi cadastro com sucesso na Sabor Express!')
    voltar_menu(lista_nomes_restaurantes)
    
def inserirListaPrato(prato1, prato1_id, prato1_nome, prato1_descricao, prato1_preco, prato1_categoria, nome_restaurante_escolhido):
    lista_prato1 = (prato1)
    lista_id_prato.append(prato1_id)
    lista_nome_prato.append(prato1_nome)
    lista_descricao_prato.append(prato1_descricao)
    lista_preco_prato.append(prato1_preco)
    lista_categoria_prato.append(prato1_categoria)
    lista_restaurante_prato.append(nome_restaurante_escolhido)
    
    print(f'Seu Prato {prato1_nome} foi cadastro com sucesso na Sabor Express!')
    voltar_menu(lista_nomes_restaurantes)
    
def cadastrarPessoa():
    nome_pessoa = input('Insira seu nome completo:\n-> ')
    idade_pessoa = input('Insira sua idade:\n-> ')
    telefone_pessoa = input('Insira seu Telefone:\n-> ')
    email_pessoa = input('Insira seu email:\n-> ')
    cpf_pessoa = input('Insira seu CPF:\n-> ')

    print(f'\n\n---|SEUS DADOS CADASTRADOS|---\n-------------------------------\nNome: {nome_pessoa}\nIdade: {idade_pessoa}\nTelefone: {telefone_pessoa}\nEmail: {email_pessoa}\nCPF: {cpf_pessoa}\n-------------------------------\n')
    dados_corretos_pessoa = Escolha(opcao_sim_nao, 'O seus dados estão corretos?\nSIM(S) ou NAO(N)\n-> ')

    if dados_corretos_pessoa == 'SIM' or dados_corretos_pessoa == 'S':
        inserirListasPessoa(nome_pessoa, idade_pessoa, telefone_pessoa, email_pessoa, cpf_pessoa)
        limpar_tela()

def cadastrar_restaurantes(lista_nomes_restaurante):
    while True:
                nome_restaurante = input('Insira o nome do seu restaurante:\n-> ')
                tipo_restaurante = input('Insira o tipo da cozinha do seu restaurante (ex: Italiana, Japonesa, etc):\n-> ')
                cnpj_restaurante = input('Insira o CNPJ do seu restaurante:\n-> ')
                telefone_restaurante = input('Insira o Telefone de Contato do seu Restaurante:\n-> ')
                email_restaurante = input('Insira o Email de Contato do seu Restaurante:\n-> ')

                print('\n---------------------\nInsira o endereço completo do seu restaurante:\n---------------------\n')
                
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

                    inserirListasRestaurante(lista_nomes_restaurantes, nome_restaurante, tipo_restaurante, cnpj_restaurante, telefone_restaurante, email_restaurante, endereco_restaurante)
                    limpar_tela()

def cadastrar_pratos_restaurantes(lista_nomes_restaurantes):
    if not lista_nomes_restaurantes:
        print('Ainda não existem Restaurantes cadastrados.')
        voltar_menu(lista_nomes_restaurantes)
    else:
        deseja_inserir_pratos = Escolha(opcao_sim_nao, 'Deseja inserir um prato a um restaurante cadastrado?:\nSIM(S) ou NAO(N)\n-> ')
        if deseja_inserir_pratos == 'SIM' or deseja_inserir_pratos == 'S':
            print('Insira seus pratos desejados:\n')
            
            
            while True:
                
                print("Escolha um dos restaurantes cadastrados:")
                for i, restaurante in enumerate(lista_nomes_restaurantes):
                    print(f"{i+1}. {restaurante}")
                
                
                escolha_restaurante = verificar_numero("Digite o número do restaurante para associar o prato:\n-> ")
                if escolha_restaurante < 1 or not lista_nomes_restaurantes:
                    print('Escolha uma opção válida.')
                
                else:
                    
                    nome_restaurante_escolhido = lista_nomes_restaurantes[escolha_restaurante - 1]
                
                    print('Detalhes do primeiro prato:')
                    prato1_id = input('Insira o Identificador Único (ID):\n-> ')
                    prato1_nome = input('Insira o nome do prato:\n-> ')
                    prato1_descricao = input('Insira a descrição do prato:\n-> ')
                    prato1_preco = input('Insira o preço do seu prato:\n-> ')
                    prato1_categoria = input('Insira a categoria (Ex. Japonês, Italiano) do seu prato:\n-> ')
                    print(f'\n--------------------------------\nSeu prato n1:\nID: {prato1_id}\nNome: {prato1_nome}\nDescrição: {prato1_descricao}\nPreço: R${prato1_preco}\nCategoria: {prato1_categoria}\n--------------------------------\n')
                    
                    dados_corretos = Escolha(opcao_sim_nao,'As informações acima do seu prato estão corretas?:\nSIM(S) ou NAO(N)\n-> ')
                    if dados_corretos == 'SIM' or dados_corretos == 'S':
                        
                        prato1 = (f'ID: {prato1_id}\nNome: {prato1_nome}\nDescrição: {prato1_descricao}\nPreço: R${prato1_preco}\nCategoria: {prato1_categoria}\n RESTAURANTE: {nome_restaurante_escolhido}')
                        
                        inserirListaPrato(prato1, prato1_id, prato1_nome, prato1_descricao, prato1_preco, prato1_categoria, nome_restaurante_escolhido)
                        
def pratos_cadastrados():
    if not lista_id_prato:
        limpar_tela()
        print('Nenhum restaurante registrado.')
    else:
        limpar_tela()
        for i in range(len(lista_id_prato)):
            print(f'\n---|PRATO {i+1}|---')
            print(f'ID: {lista_id_prato[i]}')
            print(f'Nome: {lista_nome_prato[i]}')
            print(f'Descrição: {lista_descricao_prato[i]}')
            print(f'Preço: R${lista_preco_prato[i]}')
            print(f'Categoria: {lista_categoria_prato[i]}')
            print(f'RESTAURANTE: {lista_restaurante_prato[i]}')

    voltar_menu(lista_nomes_restaurantes)

if __name__ == '__main__':
    main()