'''
068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''

import random

cont = 0
sorteio = random.randint(1, 2)
computador = random.randint(1, 2)

while True:

    if sorteio == computador:
        cont += 1
        print(f"sorteio: {sorteio} & computador: {computador}")
        sorteio = random.randint(1, 2)
        computador = random.randint(1, 2)
    else:
        print(f"sorteio: {sorteio} & computador: {computador}")
        break

print(f"O total de acertos foi de {cont}")
