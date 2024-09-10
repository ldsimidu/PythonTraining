class modelo_restaurante:
    def __init__(self, Nome, Categoria): 
        self.Nome = Nome
        self.Categoria = Categoria
        Ativo = False
    
restaurante_pizza = modelo_restaurante('Nome', 'Categoria')
restaurante_sushi = modelo_restaurante('Sushi do Lucas', 'Japones')

print(restaurante_pizza)

#definicoes 
'''
restaurante_pizza.Nome = 'Pizzaria do mario'
restaurante_pizza.Categoria = 'Italiano'
restaurante_pizza.Ativo = False'''


tipos_restaurantes = [restaurante_pizza, restaurante_sushi]

#print(dir(restaurante_pizza))
#print(vars(restaurante_pizza))
#print(f'RESTAURANTE:\n\nNome: {restaurante_pizza.Nome}\nCategoria: {restaurante_pizza.Categoria}\nAtivo: {restaurante_pizza.Ativo}')