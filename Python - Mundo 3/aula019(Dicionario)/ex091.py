'''
091: CRIE UM PROGRAMA ONDE 4 JOGADORES JOGUEM UM DADO E TENHAM RESULTADOS ALEATÓRIOS. GUARDE ESSES RESULTADOS EM UM DICIONÁRIO. NO FINAL, COLOQUE ESSE DICIONÁRIO EM ORDEM, SABENDO QUE O VENCEDOR TIROU O MAIOR NÚMERO NO DADO.
'''

from random import randint
from time import sleep

jogador = {}
jogos = []
print('Valores Sorteados: ')
for c in range(1, 5):
    jogador['jogador'] = f'Jogador{c}'
    jogador['dado'] = randint(1, 6)
    jogos.append(jogador.copy())
    print(f"{jogador['jogador']} tirou {jogador['dado']} no dado.")
    sleep(0.5)
lista_ordenada = sorted(jogos, key=lambda x: x['dado'], reverse=True)
print('-='*30)
print('     ==  RANKING DOS JOGADORES ==')
for pos, j in enumerate(lista_ordenada):
    print(f"       {pos+1}º lugar: {j['jogador']} com {j['dado']}")