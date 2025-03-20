'''
103: FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA FICHA(), QUE RECEBA DOS PARÂMETROS OPCIONAIS: O NOME DE UM JOGADOR E QUANTOS GOLS ELE MARCOU
O PROGRAMA DEVERÁ SER CAPAZ DE MOSTRAR A FICHA DO JOGADOR, MESMO QUE ALGUM DADO NÃO TENHA SIDO INFORMADO CORRETAMENTE
'''

def ficha(nome="<desconhecido>", gols=0):
        print(f"O jogador {nome} fez {gols} gols")
print('-'*40)
jogador = input("Nome do Jogador: ")
n_gols = input("Número de gols: ")
if n_gols.isnumeric():
    n_gols = int(n_gols)    
else:
    n_gols = 0
if jogador.strip() == '':
    ficha(gols=n_gols)
else:
    ficha(jogador, n_gols)


