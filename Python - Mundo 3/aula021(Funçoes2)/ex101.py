'''
101: CRIE UM PROGRAMA QUE TENHA UM FUNÇÃO CHAMADA VOTO() QUE VAI RECEBER COMO PARÂMETRO O ANO DE NASCIMENTO DE UMA PESSOA, RETORNANDO UM VALOR LITERAL INDICANDO SE UMA PESSOA TEM VOTO NEGADO, OPCIONAL OU OBRIGATÓRIO NAS ELEIÇÕES
'''

from datetime import datetime

def voto(ano):

    idade = datetime.now().year - ano
    return idade

votacao = voto(int(input("Digite seu ano de nascimento: ")))

if votacao >= 18:
    print("Voto obrigatório nas eleições!")
elif 16 <= votacao < 18:
    print("Voto opcional nas eleições!")
elif votacao < 16:
    print("Voto negado nas eleições!")