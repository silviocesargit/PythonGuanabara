'''
088: FAÇA UM PROGRAMA QUE AJUDE UM JOGADOR DA MEGA SENA A CRIAR PALPITES. O PROGRAMA VAI PERGUNTAR QUANTOS JOGOS SERÃO GERADOS E VAI SORTEAR 6 NÚMEROS ENTRE 1 E 60 PARA CADA JOGO, CADASTRANDO TUDO EM UMA LISTA COMPOSTA
'''
from random import randint

jogos = []
temporaria = []

while True:
    n_jogos = int(input("Digite o número de jogos que deseja gerar: "))
    for c in range(0, n_jogos):
        for k in range(0, 6):
            numero = randint(1, 60)
            temporaria.append(numero)
        jogos.append(temporaria[:])
        temporaria.clear()
    if len(jogos) == n_jogos:
        break
print()
print(f"Lista dos jogos: {jogos}")
print(f"Lista temporaria: {temporaria}")

