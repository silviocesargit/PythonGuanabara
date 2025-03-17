'''
095: APRIMODE O DESAFIO 093 PARA QUE ELE FUNCIONE COM VÁRIOS JOGADORES, INCLUINDO UM SISTEMA DE VISUALIZAÇÃO DE DETALHES DO APROVEITAMENTE DE CADA JOGADOR

093: CRIE UM PROGRAMA QUE GERENCIE O APROVEITAMENTO DE UM JOGADOR DE FUTEBOL. O PROGRAMA VAI LER O NOME DO JOGADOR E QUANTAS PARTIDAS ELE JOGOU. DEPOIS VAI LER A QUANTIDADE DE GOLS FEITOS EM CADA PARTIDA. NO FINAL, TUDO ISSO SERÁ GUARDADO EM UM DICIONÁRIO, INCLUINDO O TOTAL DE GOLS FEITOS DURANTE O CAMPEONATO
'''

listagem = []
jogador = {}
temporaria = []
total_gols = 0

while True:
    jogador['nome'] = input("Nome do Jogador: ").capitalize()
    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    for c in range(0, partidas):
        gol = int(input(f"    Quantos gols na partida {c+1}? "))
        temporaria.append(gol)
        total_gols += gol
    jogador['gols'] = temporaria[:]
    jogador['total'] = total_gols
    listagem.append(jogador.copy())
    temporaria.clear()
    total_gols = 0
    opcao = input("Quer continuar? [S/N] ").upper()
    if 'N' in opcao:
        break
print("-="*30)
print(f"cod  nome           gols           total")
print('-'*40)
for pos, j in enumerate(listagem):
    print(f"{pos:>3} {j['nome']}       {j['gols']}     {j['total']}")
print('-'*40)
dados_jogador = int(input("Mostrar dados de qual jogador? (999 para parar) "))
while dados_jogador != 999:
    for p, j in enumerate(listagem):
        if p == dados_jogador:
            print(f"  --  LEVANTAMENTO DO JOGADOR {j['nome']}: ")
            for p, t in enumerate(j['gols']):
                print(f"No jogo {p+1} fez {t} gols.")
    dados_jogador = int(input("Mostrar dados de qual jogador? (999 para parar) "))

        


