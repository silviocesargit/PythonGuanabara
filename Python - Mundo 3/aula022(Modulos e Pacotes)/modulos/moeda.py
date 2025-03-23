'''
107: CRIE UM MÓDULO CHAMADO moeda.py QUE TENHA AS FUNÇÕES INCORPORADAS aumentar(), diminuir(), dobro() e metade().
FAÇA TAMBÉM UM PROGRAMA QUE IMPORTE ESSE MÓDULO E USE ALGUMAS DESSAS FUNÇÕES
'''

def aumentar(num):
    aumento = num*0.1
    print(f"Aumentando 10%, temos R${aumento+num}")

def dobro(num):
    print(f"O dobro de R${num} é R${num*2}")

def metade(num):
    print(f"A metade de R${num} é R${num/2}")
