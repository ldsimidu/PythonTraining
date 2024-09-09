class Restaurante():
    nome = ""
    categoria = ""
    ativo = ""

restaurante_praca = Restaurante()
restaurante_praca.nome = 'MamaMia'
restaurante_praca.categoria = 'Italiana'
restaurante_praca.ativo = True

nome_do_restaurante = restaurante_praca.nome

if restaurante_praca.ativo:
    print('O restaurante está ativo.')
else:
    print('O restaurante está inativo.')

print(f'\nNome: {restaurante_praca.nome}\n Categoria: {restaurante_praca.categoria}\n Ativo: {restaurante_praca.ativo}')
