'''
DICIONARIOS

Para declarar um dicionário, se fosse numa lista:

dados = ['Pedro', 25]

No dicionário:

dados = {'nome':'Pedro', 'idade':25}

print(dados['nome']) --> Aqui eu vou printar o elemento que está no índice 'nome', no caso 'Pedro'

Para adicionar um novo elemento, exemplo:

dados['sexo'] = 'M' --> No dicionário não precisa do append, é só declarar o novo nome do novo indíce, e atribuir o elemento desejado

Para remover um elemento, exemplo:

del dados['idade'] -> Você define o indice do elemento que deseja remover

Existe uma diferença entre 3 definições nos dicionários, exemplo:

filme {'titulo':'Star Wars', 
        'ano': 1977, 
        'diretor': 'George Lucas'}

print(filme.values()) --> Values (valores) vai pegar os elementos dos indices - Star Wars, 1977, George Lucas

print(filme.keys()) --> keys (chaves) vai pegar os nomes dos indices que você atribuiu - titulo, ano, diretor

print(filme.items()) --> items (tudo) vai pegar tanto os indices (keys) quanto os elementos (values)

Da pra usar esses conceitos nos laços, por exemplo um enumerate, exemplo:

for k, v in filme.items() --> Ou seja, pra cada chave (keys) e valor (values) dentro de items (tudo)
    print(f'O {k} é {v}')

Pode juntar lista, tuplas e dicionários!

Por exemplo, dá pra criar uma lista, onde cada elemento da lista é um dicionário

locadora = [{'titulo':'Star Wars', 'ano': 1977, 'diretor':'George Lucas'}]

print(locadora[0]['ano']) --> Quer dizer, na posição 0 da lista, e na posição 'ano' do dicionário

Para criar uma cópia de um dicionário:

locadora.append(filme.copy())

Outro exemplo de for:

for l in locadora:
    for v in filme.values():

    
DESAFIOS:

090: FAÇA UM PROGRAMA QUE LEIA NOME E MÉDIA DE UM ALUNO, GUARDANDO TAMBÉM A SITUAÇÃO EM UM DICIONÁRIO. NO FINAL, MOSTRE O CONTEÚDO DA ESTRUTURA NA TELA

091: CRIE UM PROGRAMA ONDE 4 JOGADORES JOGUEM UM DADO E TENHAM RESULTADOS ALEATÓRIOS. GUARDE ESSES RESULTADOS EM UM DICIONÁRIO. NO FINAL, COLOQUE ESSE DICIONÁRIO EM ORDEM, SABENDO QUE O VENCEDOR TIROU O MAIOR NÚMERO NO DADO.

092: CRIE UM PROGRAMA QUE LEIA NOME, ANO DE NASCIMENTO E CARTEIRA DE TRABALHO E CADASTRE-OS (COM IDADE) EM UM DICIONÁRIO SE POR ACASO A CTPS FOR DIFERENTE DE ZERO, O DICIONÁRIO RECEBERÁ TAMBÉM O ANO DE CONTRATAÇÃO E O SALÁRIO. CALCULE E ACRESCENTE, ALÉM DA IDADE, COM QUANTOS ANOS A PESSOA VAI SE APOSENTAR

093: CRIE UM PROGRAMA QUE GERENCIE O APROVEITAMENTO DE UM JOGADOR DE FUTEBOL. O PROGRAMA VAI LER O NOME DO JOGADOR E QUANTAS PARTIDAS ELE JOGOU. DEPOIS VAI LER A QUANTIDADE DE GOLS FEITOS EM CADA PARTIDA. NO FINAL, TUDO ISSO SERÁ GUARDADO EM UM DICIONÁRIO, INCLUINDO O TOTAL DE GOLS FEITOS DURANTE O CAMPEONATO

094: CRIE UM PROGRAMA QUE LEIA NOME, SEXO E IDADE DE VÁRIAS PESSOAS, GUARDANDO OS DADOS DE CADA PESSOA EM UM DICIONÁRIO E TODOS OS DICIONÁRIOS EM UMA LISTA. NO FINAL, MOSTRE:
A) QUANTAS PESSOAS FORAM CADASTRADAS
B) A MÉDIA DE IDADE DO GRUPO
C) A MÉDIA DE IDADE DO GRUPO
D) UMA LISTA COM TODAS AS PESSOAS COM IDADE ACIMA DA MÉDIA

095: APRIMODE O DESAFIO 093 PARA QUE ELE FUNCIONE COM VÁRIOS JOGADORES, INCLUINDO UM SISTEMA DE VISUALIZAÇÃO DE DETALHES DO APROVEITAMENTE DE CADA JOGADOR


'''