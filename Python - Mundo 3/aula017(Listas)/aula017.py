'''
lista = []

del lanche[*] -> Utiliza o índice para remover o elemento desejado
lanche.pop() -> Se deixar em branco, ele vai remover o último elemento, caso queiro um elemento específico, é só informar o índice do mesmo
lanche.remove() -> Aqui você não utiliza o índice, mas sim o valor que está contido na lista e você deseja remover. Detalhe, ele vai remover a primeira ocorrência daquele valor na lista

Existe a possibilidade de fazer isso aqui: valores = list(range(4, 11)) o resultado será que: valores = [4, 5, 6, 7, 8, 9, 10]

valores.sort() -> Coloca os valores em ordem crescente
valores.sort(reverse=True) -> Coloca os valore em ordem decrescente

valores.insert(8, 11) -> Isso significa que Na posição 8, eu desejo inserir o elemntro 11

Existe uma forma de fazer uma ligação de uma lista com a outra, e quando você mexe em uma, afeta a outra da mesma maneira:
Ex:
lista1 = [1, 2, 3, 4]
lista2 = lista1

Se eu não quiser que exista essa ligação, é só criar uma cópia de uma lista para a outra:
Ex:
lista1 = [1, 2, 3, 4]
lista2 = lista1[:]

Desafios:
078: FAÇA UM PROGRAMA QUE LEIA 5 VALORES NUMÉRICOS E GUARDE-OS EM UMA LISTA
NO FINAL, MOSTRE QUAL FOI O MAIOR E O MENOR VALOR DIGITADO E AS SUAS RESPECTIVAS POSIÇÕES NA LISTA

079: CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR VÁRIOS VALORES NUMÉRICOS E CADASTRE-OS EM UMA LISTA. CASO O NÚMERO JÁ EXISTA LÁ DENTRO, ELE NÃO SERÁ ADICIONADO. NO FINAL, SERÃO EXIBIDOS TODOS OS VALORES ÚNICOS DIGITADOR, EM ORDEM CRESCENTE.

080: CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR CINCO VALORES NUMÉRICOS E CADASTRE-OS EM UMA LISTA, JÁ NA POSIÇÃO CORRETA DE INSERÇÃO (SEM USAR O SORT())
NO FINAL, MOSTRE A LISTA ORDENADA NA TELA

081: CRIE UM PROGRAMA QUE VAI LER VÁRIOS NÚMEROS E COLOCAR EM UMA LISTA
DEPOIS DISSO, MOSTRE:
A) QUANTOS NÚMEROS FORAM DIGITADOS
B) A LISTA DE VALORES, ORDENADA DE FORMA DESCRESCENTE
C) SE O VALOR 5 FOI DIGITADO E ESTÁ OU NÃO NA LISTA

082: CRIE UM PROGRAMA QUE VAI LER VÁRIOS NÚMEROS E COLOCAR EM UMA LISTA
DEPOIS DISSO, CRIE DUAS LISTAS EXTRAS QUE VÃO CONTER APENAS OS VALORES PARES E OS VALORES ÍMPARES DIGITADOS, RESPECTIVAMENTE
AO FINAL, MOSTRE O CONTEÚDO DAS TRÊS LISTAS GERADAS

083: CRIE UM PROGRAMA ONDE O USUÁRIO DIGITE UMA EXPRESSÃO QUALQUER QUE USE PARÊNTESES, SEU APLICATIVO DEVERÁ ANALISAR SE A EXPRESSÃO PASSADA ESTÁ COM OS PARÊNTESES ANERTOS E FECHADOS NA ORDEM CORRETA
'''