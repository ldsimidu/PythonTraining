opcao_sim_nao = ['Sim', 'S', 'NAO', 'N']
opcao_tipo_cadastro = ['Pessoa', 'P', 'Restaurante', 'R']

def Escolha(lista_opcoes, msg):
    escolha = input(msg).upper()
    while escolha not in lista_opcoes:
        print('\nEscolha uma opção válida\n')
        escolha = input(msg).upper()
    return escolha

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

cadastro_sim_nao = Escolha(opcao_sim_nao, 'Deseja cadastrar-se?:\nSIM(S) ou NAO(N)\n-> ')

if cadastro_sim_nao == 'SIM' or cadastro_sim_nao == 'S':
    
    while True:
        tipo_cadastro = Escolha(opcao_tipo_cadastro, '\nVocê deseja se cadastrar como:\nPESSOA(P) ou RESTAURANTE(R)?\n-> ')

        if tipo_cadastro == 'PESSOA' or tipo_cadastro == 'P':
            print('\nVocê escolheu se cadastrar como:\nPESSOA\n')
        else:
            print('\nVocê escolheu se cadastrar como:\nRESTAURANTE\n')

        continuar_cadastro = Escolha(opcao_sim_nao, 'Deseja continuar com o perfil desejado para cadastro?\nSIM(S) ou NAO(N)\n\n-> ')

        if continuar_cadastro == 'SIM' or continuar_cadastro == 'S':
            while True:
                if tipo_cadastro == 'PESSOA' or tipo_cadastro == 'P':
                    nome_pessoa = input('Insira seu nome completo:\n-> ')
                    idade_pessoa = input('Insira sua idade:\n-> ')
                    email_pessoa = input('Insira seu email:\n-> ')
                    cpf_pessoa = input('Insira seu CPF:\n-> ')

                    print(f'\n\n---|SEUS DADOS CADASTRADOS|---\n-------------------------------\nNome: {nome_pessoa}\nIdade: {idade_pessoa}\nEmail: {email_pessoa}\nCPF: {cpf_pessoa}\n-------------------------------\n')
                    dados_corretos_pessoa = Escolha(opcao_sim_nao, 'O seus dados estão corretos?\nSIM(S) ou NAO(N)\n\n-> ')

                    if dados_corretos_pessoa == 'SIM' or dados_corretos_pessoa == 'S':
                        print('JNAJDWNANDJSNDA')


                else:
                    nome_restaurante = input('Insira o nome do seu restaurante:\n-> ')
                    tipo_restaurante = input('Insira o tipo da cozinha do seu restaurante (ex: Italiana, Japonesa, etc):\n-> ')

                    print('Insira o endereço completo do seu restaurante:\n')
                    while True:
                        estado_restaurante = input('Insira o ESTADO do seu Restaurante:\n-> ')
                        cidade_restaurante = input('Insira a CIDADE do seu Restaurante:\n-> ')
                        bairro_restaurante = input('Insira o BAIRRO do seu Restaurante:\n-> ')
                        rua_restaurante = input('Insira a RUA do seu Restaurante:\n-> ')
                        numero_restaurante = input('Insira o NÚMERO do seu Restaurante:\n-> ')

                        print(f'---|DADOS DO ENDEREÇO|---\n-------------------------------\n\nSeu Restaurante pertence a: {estado_restaurante}, {cidade_restaurante}, {bairro_restaurante}, {rua_restaurante}, {numero_restaurante}.\n\n-------------------------------\n\n')

                        dados_corretos_restaurante = Escolha(opcao_sim_nao, 'Os dados do endereço acima estão corretos?\nSIM(S) ou NAO(N)\n\n-> ')

                        if dados_corretos_restaurante == 'SIM' or dados_corretos_restaurante == 'S':

                            endereco_restaurante = (f'{estado_restaurante}, {cidade_restaurante}, {bairro_restaurante}, {rua_restaurante}, {numero_restaurante}')

                            cnpj_restaurante = input('Insira o CNPJ do seu restaurante:\n-> ')
                            telefone_restaurante = input('Insira o Telefone de Contato do seu Restaurante:\n-> ')
                            email_restaurante = input('Insira o Email de Contato do seu Restaurante:\n-> ')
else:
    print('''

▒█▀▄▀█ ▒█▀▀▀ ▒█▄░▒█ ▒█░▒█ 
▒█▒█▒█ ▒█▀▀▀ ▒█▒█▒█ ▒█░▒█ 
▒█░░▒█ ▒█▄▄▄ ▒█░░▀█ ░▀▄▄▀
          \n\n''')

    print('1. Cadastrar Restaurante')


                        

                
            

         