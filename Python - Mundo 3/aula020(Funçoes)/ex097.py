'''
097: FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA ESCREVE(), QUE RECEBA UM TEXTO QUALQUER COMO PARÂMETRO E MOSTRE UMA MENSAGEM COM TAMANHO ADAPTÁVEL
EX:
ESCREVA('OLÁ, MUNDO!')
SAÍDA:
-----------------
OLÁ, MUNDO!
-----------------
'''

def escreve(txt):
    print(f"-"*len(txt))
    print(txt)
    print(f"-"*len(txt))

escreve("A minha mãe mandou dizer que você não vale nada")