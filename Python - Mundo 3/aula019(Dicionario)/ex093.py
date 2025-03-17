'''
093: CRIE UM PROGRAMA QUE GERENCIE O APROVEITAMENTO DE UM JOGADOR DE FUTEBOL. O PROGRAMA VAI LER O NOME DO JOGADOR E QUANTAS PARTIDAS ELE JOGOU. DEPOIS VAI LER A QUANTIDADE DE GOLS FEITOS EM CADA PARTIDA. NO FINAL, TUDO ISSO SERÁ GUARDADO EM UM DICIONÁRIO, INCLUINDO O TOTAL DE GOLS FEITOS DURANTE O CAMPEONATO
'''

dados = {}
lista_gols = []
total_gols = 0

dados['nome'] = input('Nome do Jogador: ')
partidas = int(input(f"Quantas partidas {dados['nome']} jogou: "))
for c in range(0, partidas):
    lista_gols.append(int(input(f"    Quantos gols na partida {c+1}: ")))
    total_gols += lista_gols[c]
dados['gols'] = lista_gols[:]
dados['total'] = total_gols
print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f"O campo {k} tem valor {v}")
print('-='*30)
print(f"O jogador {dados['nome']} jogou {partidas} partidas")
for pos, v in enumerate(lista_gols):
    print(f"    => Na partida {pos}, fez {v} gols")
print(f"Foi um total de {total_gols}")