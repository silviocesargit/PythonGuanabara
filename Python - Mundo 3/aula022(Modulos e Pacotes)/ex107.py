'''
107: CRIE UM MÓDULO CHAMADO moeda.py QUE TENHA AS FUNÇÕES INCORPORADAS aumentar(), diminuir(), dobro() e metade().
FAÇA TAMBÉM UM PROGRAMA QUE IMPORTE ESSE MÓDULO E USE ALGUMAS DESSAS FUNÇÕES
'''

from modulos import moeda

n = float(input("Digite o preço: R$"))
moeda.metade(n)
moeda.dobro(n)
moeda.aumentar(n)