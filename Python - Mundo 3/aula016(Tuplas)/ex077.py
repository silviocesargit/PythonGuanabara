'''
077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

tupla = ('GELO', 'GARRAFA', 'SOBREMESA', 'CALCINHA', 'PERFUME')
vogais = ('A', 'E', 'I', 'O', 'U')

for c in range(0, len(tupla)):
    nome = tupla[c]
    print(f'O nome {nome} possui as vogais:', end=' ')
    for letra in nome:
        if letra in vogais:
            print(letra, end=' ')