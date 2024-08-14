import os
from lists import *

def main():
    menu_principal(lista_nomes_restaurantes)   
    
def verificar_numero(msg):
    while True:
        numero = input(msg)
        if not numero.isnumeric():
            print('O valor inserido não é válido.')
        else:
            return int(numero)
    
def finalizar_app():
    os.system('cls')
    # os.system('clear') 
    print('Finalizando o app')
    exit()

def limpar_tela():
    os.system('cls')
    
def escolha(lista_opcoes, msg):
    escolha = input(msg).upper()
    while escolha not in lista_opcoes:
        print('\nEscolha uma opção válida\n')
        escolha = input(msg).upper()
    return escolha

def voltar_menu():
    #voltar_menu = Escolha(opcao_voltar, 'Pressione a TECLA "B" para voltar ao Menu:\nVoltar(B)\n-> ')
    input('\nDigite uma tecla para voltar ao menu ')
    limpar_tela()
    main()

def deseja_listar_restaurante_ou_prato():
    restaurante_ou_prato = escolha(opcao_restaurante_prato, 'Deseja listar:\nRESTAURANTES(R) ou PRATOS(P)\n-> ')
    if restaurante_ou_prato == 'RESTAURANTE' or restaurante_ou_prato == 'R':
        restaurantes_cadastrados()
        limpar_tela()
    else:
        pratos_cadastrados()
        limpar_tela()
    
def deseja_cadastrar_restaurante_prato(lista_nomes_restaurantes):
    restaurante_ou_prato = escolha(opcao_restaurante_prato, 'Deseja Cadastrar:\nRESTAURANTES(R) ou PRATOS(P)\n-> ')
    if restaurante_ou_prato == 'RESTAURANTE' or restaurante_ou_prato == 'R':
        limpar_tela()
        cadastrar_restaurantes(lista_nomes_restaurantes)
    else:
        limpar_tela()
        cadastrar_pratos_restaurantes(lista_nomes_restaurantes)
            
def menu_principal(lista_nomes_restaurantes):
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n""")

    
    print('-----|MENU|-----\n1. Sua Conta\n2. Cadastrar Novo Restaurante/Prato\n3. Listar Restaurantes/Pratos\n4. Ativar Restaurante\n5. Sobre Nós\n6. Sair do Aplicativo\n----------------\n')

    escolher_menu = escolha(opcao_menu, 'Qual opção deseja escolher? (1 / 2 / 3 / 4 / 5 / 6)\n-> ')
    if escolher_menu == '6':
        finalizar_app()
    elif escolher_menu == '2':
        deseja_cadastrar_restaurante_prato(lista_nomes_restaurantes)
    elif escolher_menu == '3':
        deseja_listar_restaurante_ou_prato()
    elif escolher_menu == '4':
        print('não cheguei nessa parte do curso ainda irmão')
    elif escolher_menu == '5':
        sobre_nos()
    else:
        sua_conta() 

def sobre_nos():
    sobre = [
    {
        'nome': 'SaborExpress',
        'descricao': 'Um aplicativo que conecta usuários a uma variedade de restaurantes locais para entrega de comida de forma rápida e fácil.',
        'features': {
            'cadastro_de_usuarios': 'Permite usuários criarem e gerenciarem suas contas.',
            'cadastro_de_restaurantes': 'Permite os restaurantes interessados se cadastrarem e incluírem seus pratos principais.',
            'visualizacao_menu': 'Permite que os usuários naveguem pelos menus e selecionem itens para entrega.',
            'rastreamento_pedido': 'Fornece rastreamento em tempo real dos pedidos do restaurante até a localização do usuário.',
            'opcao_pagamento': ['Pix', 'Débito', 'Crédito', 'PayPal'],
            'avalicao': 'Os usuários podem avaliar sua experiência e deixar comentários sobre os restaurantes.'
        }
    },
    {
        'papeis_usuario': {
            'cliente': 'Pode navegar pelos restaurantes, fazer pedidos e acompanhar as entregas.',
            'dono_restaurante': 'Pode gerenciar o menu do restaurante, visualizar pedidos e atualizar o status.',
            'entregador': 'Pode visualizar entregas disponíveis, aceitá-las e atualizar o status da entrega.'
        }
    },
    {
        'plataformas': ['iOS', 'Android', 'Web'],
        'data_lancamento': '2024',
        'develop': 'NEW ERA CROWMA'
    }
]

# Exibindo as informações do app SaborExpress
    print(f"Nome do App: {sobre[0]['nome']}")
    print(f"Descrição: {sobre[0]['descricao']}")
    print(f"Funcionalidades: {', '.join(sobre[0]['features'].keys())}")
    print(f"Papéis de Usuários: {', '.join(sobre[1]['papeis_usuario'].keys())}")
    print(f"Plataformas Suportadas: {', '.join(sobre[2]['plataformas'])}")
    print(f"Ano de Lançamento: {sobre[2]['data_lancamento']}")
    print(f"Desenvolvedora: {sobre[2]['develop']}")

    voltar_menu()

def sua_conta():

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
        '''editar_dados = escolha(opcao_sim_nao, 'Deseja editar seus dados?:\nSIM(S) ou NAO(N)\n-> ')
        if editar_dados == 'SIM' or editar_dados == 'S':
            cadastrar_pessoa()'''
        
        voltar_menu()

def restaurantes_cadastrados():

    if not lista_nomes_restaurantes:
        limpar_tela()
        print('Nenhum restaurante registrado.')
    else:
        limpar_tela()
        for i in range(len(lista_nomes_restaurantes)):
            print(f'\n---|RESTAURANTE {i+1}|---')
            print(f'Nome: {lista_nomes_restaurantes[i]}')
            print(f'Tipo: {lista_categoria_restaurantes[i]}')
            print(f'CNPJ: {lista_cnpj_restaurantes[i]}')
            print(f'Telefone: {lista_telefone_restaurantes[i]}')
            print(f'Email: {lista_email_restaurantes[i]}')
            print(f'Endereço: {lista_endereco_restaurantes[i]}\n')

    voltar_menu()
    
def deseja_cadastrar_conta():
    #while True:
    deseja_cadastro = escolha(opcao_sim_nao, 'Deseja cadastrar-se?:\nSIM(S) ou NAO(N)\n-> ')
    if deseja_cadastro == 'SIM' or deseja_cadastro == 'S':
        '''tipo_cadastro = escolha(opcao_tipo_cadastro, '\nVocê deseja se cadastrar uma:\nCONTA(P) ou RESTAURANTE(R)?\n-> ')

        if tipo_cadastro == 'PESSOA' or tipo_cadastro == 'P':
            print('\nVocê escolheu se cadastrar uma:\nCONTA\n')
        else:
            print('\nVocê escolheu se cadastrar um :\nRESTAURANTE\n')'''

        '''continuar_cadastro = escolha(opcao_sim_nao, 'Deseja continuar com o perfil desejado para cadastro?\nSIM(S) ou NAO(N)\n-> ')
        if continuar_cadastro == 'SIM' or continuar_cadastro == 'S':'''
        limpar_tela()    
        while True:
            cadastrar_pessoa()
            
    else:
        limpar_tela()
        menu_principal(lista_nomes_restaurantes)

def inserir_listas_pessoa(nome_pessoa, idade_pessoa, telefone_pessoa, email_pessoa, cpf_pessoa):
    usuario_cadastrado = True
    lista_nomes_pessoas.append(nome_pessoa)
    lista_idade_pessoas.append(idade_pessoa)
    lista_telefone_pessoas.append(telefone_pessoa)
    lista_email_pessoas.append(email_pessoa)
    lista_cpf_pessoas.append(cpf_pessoa)

    print(f'Seja muito Bem-Vindo(a), {nome_pessoa}! A Sabor Express fica feliz em te receber!')
    voltar_menu()

def inserir_listas_restaurante(lista_nomes_restaurantes, nome_restaurante, tipo_restaurante, cnpj_restaurante, telefone_restaurante, email_restaurante, endereco_restaurante):

    usuario_cadastrado = True
    lista_nomes_restaurantes.append(nome_restaurante)
    lista_categoria_restaurantes.append(tipo_restaurante)
    lista_cnpj_restaurantes.append(cnpj_restaurante)
    lista_telefone_restaurantes.append(telefone_restaurante)
    lista_email_restaurantes.append(email_restaurante)
    lista_endereco_restaurantes.append(endereco_restaurante)

    print(f'Seu Restaurante {nome_restaurante} foi cadastro com sucesso na Sabor Express!')
    
    voltar_menu()

def inserir_listas_prato(prato1, prato1_id, prato1_nome, prato1_descricao, prato1_preco, prato1_categoria, nome_restaurante_escolhido):
    lista_prato1 = (prato1)
    lista_id_prato.append(prato1_id)
    lista_nome_prato.append(prato1_nome)
    lista_descricao_prato.append(prato1_descricao)
    lista_preco_prato.append(prato1_preco)
    lista_categoria_prato.append(prato1_categoria)
    lista_restaurante_prato.append(nome_restaurante_escolhido)
    
    print(f'Seu Prato {prato1_nome} foi cadastro com sucesso na Sabor Express!')
    voltar_menu()

def cadastrar_pessoa():
    nome_pessoa = input('Insira seu nome completo:\n-> ')
    idade_pessoa = verificar_numero('Insira sua idade:\n-> ')
    telefone_pessoa = verificar_numero('Insira seu Telefone:\n-> ')
    email_pessoa = input('Insira seu email:\n-> ')
    cpf_pessoa = verificar_numero('Insira seu CPF:\n-> ')

    print(f'\n\n---|SEUS DADOS CADASTRADOS|---\n-------------------------------\nNome: {nome_pessoa}\nIdade: {idade_pessoa}\nTelefone: {telefone_pessoa}\nEmail: {email_pessoa}\nCPF: {cpf_pessoa}\n-------------------------------\n')
    dados_corretos_pessoa = escolha(opcao_sim_nao, 'O seus dados estão corretos?\nSIM(S) ou NAO(N)\n-> ')

    if dados_corretos_pessoa == 'SIM' or dados_corretos_pessoa == 'S':
        inserir_listas_pessoa(nome_pessoa, idade_pessoa, telefone_pessoa, email_pessoa, cpf_pessoa)
        voltar_menu(lista_nomes_restaurantes)

def categoria_restaurante():
    print('\n--------------------------------\n')
    for i, categoria in enumerate(lista_culinarias):
        print(f'{i+1}. {categoria}')
    print('\n--------------------------------\n')
    tipo_restaurante = verificar_numero('Insira o tipo da cozinha do seu restaurante:\n-> ')
    if 1 <= tipo_restaurante <= len(lista_culinarias):
        
        '''1. 1 <= tipo_restaurante: Esta parte verifica se o valor de tipo_restaurante é maior ou igual a 1. Isso é importante porque os índices das opções de culinária começam em 1.

        2. tipo_restaurante <= len(lista_culinarias): Esta parte verifica se o valor de tipo_restaurante é menor ou igual ao número total de itens na lista lista_culinarias. A função len(lista_culinarias) retorna o número de elementos na lista, e a comparação assegura que o valor inserido não exceda o número de opções disponíveis.

        3. Conjunção das comparações: Usando a notação 1 <= tipo_restaurante <= len(lista_culinarias), o código verifica simultaneamente se tipo_restaurante está dentro do intervalo válido (entre 1 e o número total de categorias na lista).'''
        limpar_tela()
        return lista_culinarias[tipo_restaurante - 1]
        
    else:
        print("Opção inválida. Por favor, selecione uma das opções listadas.")
        return categoria_restaurante()

def cadastrar_restaurantes(lista_nomes_restaurante):
    while True:
        nome_restaurante = input('Insira o nome do seu restaurante:\n-> ')
        tipo_restaurante = categoria_restaurante()
        cnpj_restaurante = verificar_numero('Insira o CNPJ do seu restaurante:\n-> ')
        telefone_restaurante = verificar_numero('Insira o Telefone de Contato do seu Restaurante:\n-> ')
        email_restaurante = input('Insira o Email de Contato do seu Restaurante:\n-> ')

        print('\n---------------------\nInsira o endereço completo do seu restaurante:\n---------------------\n')
        
        estado_restaurante = input('Insira o ESTADO do seu Restaurante:\n-> ')
        cidade_restaurante = input('Insira a CIDADE do seu Restaurante:\n-> ')
        bairro_restaurante = input('Insira o BAIRRO do seu Restaurante:\n-> ')
        rua_restaurante = input('Insira a RUA do seu Restaurante:\n-> ')
        numero_restaurante = verificar_numero('Insira o NÚMERO do seu Restaurante:\n-> ')

        print(f'\n---|DADOS DO ENDEREÇO|---\n-------------------------------\n\nSeu Restaurante pertence a: {estado_restaurante}, {cidade_restaurante}, {bairro_restaurante}, {rua_restaurante}, {numero_restaurante}.\n\n-------------------------------\n\n')

        dados_corretos_endereco_restaurante = escolha(opcao_sim_nao, 'Os dados do endereço acima estão corretos?\nSIM(S) ou NAO(N)\n\n-> ')

        if dados_corretos_endereco_restaurante == 'SIM' or dados_corretos_endereco_restaurante == 'S':
            limpar_tela()
            endereco_restaurante = (f'{estado_restaurante}, {cidade_restaurante}, {bairro_restaurante}, {rua_restaurante}, {numero_restaurante}')

            print(f'\n\n---|SEUS DADOS CADASTRADOS|---\n-------------------------------\nRazão Social: {nome_restaurante}\nCozinha: {tipo_restaurante}\nCNPJ: {cnpj_restaurante}\nTelefone: {telefone_restaurante}\nEmail: {email_restaurante}\nEndereço Completo: {endereco_restaurante}\n-------------------------------\n')

            inserir_listas_restaurante(lista_nomes_restaurantes, nome_restaurante, tipo_restaurante, cnpj_restaurante, telefone_restaurante, email_restaurante, endereco_restaurante)
            limpar_tela()

def cadastrar_pratos_restaurantes(lista_nomes_restaurantes):
    if not lista_nomes_restaurantes:
        print('Ainda não existem Restaurantes cadastrados.')
        voltar_menu()
    else:
        deseja_inserir_pratos = escolha(opcao_sim_nao, 'Deseja inserir um prato a um restaurante cadastrado?:\nSIM(S) ou NAO(N)\n-> ')
        if deseja_inserir_pratos == 'SIM' or deseja_inserir_pratos == 'S':
            print('Insira seus pratos desejados:\n')
            
            while True:
                
                print("escolha um dos restaurantes cadastrados:")
                for i, restaurante in enumerate(lista_nomes_restaurantes):
                    print(f"\n-----------------------------\n{i+1}. {restaurante}\n-----------------------------\n")
                
                escolha_restaurante = verificar_numero("Digite o número do restaurante para associar o prato:\n-> ")
                if escolha_restaurante < 1 or not lista_nomes_restaurantes:
                    print('escolha uma opção válida.')
                
                else:
                    
                    nome_restaurante_escolhido = lista_nomes_restaurantes[escolha_restaurante - 1]
                
                    print('Detalhes do primeiro prato:')
                    prato1_id = input('Insira o Identificador Único (ID):\n-> ')
                    prato1_nome = input('Insira o nome do prato:\n-> ')
                    prato1_descricao = input('Insira a descrição do prato:\n-> ')
                    prato1_preco = input('Insira o preço do seu prato:\n-> ')
                    prato1_categoria = categoria_restaurante()
                    print(f'\n--------------------------------\nSeu prato n1:\nID: {prato1_id}\nNome: {prato1_nome}\nDescrição: {prato1_descricao}\nPreço: R${prato1_preco}\nCategoria: {prato1_categoria}\n--------------------------------\n')
                    
                    dados_corretos = escolha(opcao_sim_nao,'As informações acima do seu prato estão corretas?:\nSIM(S) ou NAO(N)\n-> ')
                    if dados_corretos == 'SIM' or dados_corretos == 'S':
                        
                        prato1 = (f'ID: {prato1_id}\nNome: {prato1_nome}\nDescrição: {prato1_descricao}\nPreço: R${prato1_preco}\nCategoria: {prato1_categoria}\n RESTAURANTE: {nome_restaurante_escolhido}')
                        
                        inserir_listas_prato(prato1, prato1_id, prato1_nome, prato1_descricao, prato1_preco, prato1_categoria, nome_restaurante_escolhido)

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

    voltar_menu()

if __name__ == '__main__':
    limpar_tela()
    main()