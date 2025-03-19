'''
FUNÇÕES PARTE 2 VEREMOS:

-> INTERACTIVE HELP
-> DOCSTINGS
-> ARGUMENTOS OPCIONAIS
-> ESCOPO DE VARIÁVEIS
-> RETORNO DE RESULTADOS

* INTERACTIVE HELP (AJUDA INTERATIVA):

help() -> função em pyhon, onde você pode passar qual função padrão em python você tem dúvidas. Ele vai abrir o terminal te explicando como funciona

print(input.__doc__) -> funciona de forma semelhante ao help

* DOCSTRINGS (STRING DE DOCUMENTAÇÃO):

FUNCIONA SEMELHANTE AO HELP(), CONTUDO É VOCÊ QUEM VAI ALIMENTAR AS INFORMAÇÕES PERTINENTES AO USO DA FUNÇÃO CRIADA

PARA UTILIZÁ-LA, DIGITE ASPAS DUPLAS 3 VEZES ANTES DE INICIAR O PROGRAMA (""")
EX:
def contador(i, f, p):
    """
    -> FAZ UMA CONTAGEM E MOSTRA NA TELA
    :PARAM I: INÍCIO DA CONTAGEM
    :PARAM F: FIM DA CONTAGEM
    :PARAM P: PASSO DA CONTAGEM
    :RETURN: SEM RETORNO
    """
    c = i
    while c<= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')

help(contador)

* ARGUMENTOS OPCIONAIS (OU PARÂMETROS OPCIONAIS)

EX: 
def somar(a=0, b=0, c=0): --> Ao colocar c=0 significa que se c não receber nenhum número, c receberá 0 como parâmetro.
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 2, 5)
somar(8, 4) -> Aqui vai utilizar um parâmetro opcional
somar(b=4, c=2) -> Dessa forma eu consigo especificar quais elementos eu quero trabalhar no parâmetro, sem considerar a ordem

* ESCOPO DE VARIÁVEIS (ONDE UMA VARIÁVEL IRÁ EXISTIR, E ONDE NÃO)
EX:

def teste():
    global n -> Isso significa que a variável de dentro da função funcionará dentro e fora da função

    n = 8

    x = 8 --> Essa variável é LOCAL, e só terá validade dentro da função
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

# Programa principal
n = 2 --> Essa variável significa que é uma variável GLOBAL, pois está fora da função
print(f"No programa principal, n vale {n}")
teste()


* RETORNO DE VALORES 
EX:

def somar(a=0,  b=0, c=0):
    s = a + b + c
    return s

resp = somar(3, 2, 5) --> AO FAZER ESSA OPERAÇÃO, ESTOU DIZENDO QUE O RESULTADO DE S, OU SEJA, QUE ESTÁ DENTRO DA FUNÇÃO, SERÁ ATRIBUÍDO A UMA VARIÁVEL, NO CASO "RESP"

print(somar(3, 2, 5)) -> Posso fazer assim também

r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)

print(f"Meus cálculos deram {r1}, {r2} e {r3}") --> Posso fazer assim também

Outro Exemplo:

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')


DESAFIOS:

101: CRIE UM PROGRAMA QUE TENHA UM FUNÇÃO CHAMADA VOTO() QUE VAI RECEBER COMO PARÂMETRO O ANO DE NASCIMENTO DE UMA PESSOA, RETORNANDO UM VALOR LITERAL INDICANDO SE UMA PESSOA TEM VOTO NEGADO, OPCIONAL OU OBRIGATÓRIO NAS ELEIÇÕES

102: CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO FATORIAL() QUE RECEBA DOIS PARÂMETROS: O PRIMEIRO QUE INDIQUE O NÚMERO A CALCULAR E O OUTRO CHAMADO SHOW, QUE SERÁ UM VALOR LÓGICO (OPCIONAL) INDICANDO SE SERÁ MOSTRADO OU NÃO NA TELA O PROCESSO DE CÁLCULO DO FATORIAL

103: FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA FICHA(), QUE RECEBA DOS PARÂMETROS OPCIONAIS: O NOME DE UM JOGADOR E QUANTOS GOLS ELE MARCOU
O PROGRAMA DEVERÁ SER CAPAZ DE MOSTRAR A FICHA DO JOGADOR, MESMO QUE ALGUM DADO NÃO TENHA SIDO INFORMADO CORRETAMENTE

104: CRIE UM PROGRAMA QUE TENHA A FUNÇÃO LEAINT(), QUE VAI FUNCIONAR DE FORMA SEMELHANTE À FUNÇÃO INPUT() DO PYTHON. SÓ QUE FAZENDO A VALIDAÇÃO PARA ACEITAR APENAS UM VALOR NUMÉRICO.
EX:
N = LEIAINT('DIGITE UM N')

105: FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO NOTAS() QUE PODE RECEBER VÁRIAS NOTAS DE ALUNOS E VAI RETORNAR UM DICIONÁRIO COM AS SEGUINTES INFORMAÇÕES:
- QUANTIDADE DE NOTAS
- A MAIOR NOTA
- A MENOR NOTA
- A MÉDIA DA TURMA
- A SITUAÇÃO (OPCIONAL)

ADICIONE TAMBÉM AS DOCSTRINGS DA FUNÇÃO

106: FAÇA UM MNI-SISTEMA QUE UTILIZE O INTERACTIVE HELP DO PYTHON. O USUÁRIO VAI DIGITAR O COMANDO E O MANUAL VAI APARECER. QUANDO O USUÁRIO DIGITAR A PALAVRA 'FIM', O PROGRAMA SE ENCERRARÁ
OBS: USE CORES

'''

