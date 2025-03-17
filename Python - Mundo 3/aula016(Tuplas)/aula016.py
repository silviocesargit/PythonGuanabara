'''
AS TUPLAS SÃO IMUTÁVEIS, OU SEJA, NÃO DÁ PRA MANIPULAR OS ELEMENTROS DENTRO DELA

Na hora de referenciar um elemento, usa-se o [], independente se for tupla ou lista

Ex: lanche = (suco, pizza, sorvete)
print(lanche[1]) = pizza

Se eu colocar -1, no print acima, ele vai começar pelo final. O mesmo serve para os caso sucessivos

Ex: print(lanche[-1]) = sorvete
print(lanche[-3]) = suco
print(lanche[-2:]) = pizza, sorvete
etc...

Exemplos de for com tuplas:

for cont in range(0, len(lanche)):
posso usar o cont, pra indicar a posição, ou o lanche[cont] pra indicar o elemento na posição cont
ou
for comida in lanche:
comida = apenas o elementro da tupla
ou
for pos, comida in enumerate(lanche):
pos = posição do elementro
comida = elemento da tupla

* len(lanche) -> indica o tamanho da tupla
* sorted(lanche) -> ordena em ordem alfábetica

lanche.count(suco) --> retorna quantas vezes o elemento apareceu dentro da tupla
lanche.index(suco) --> mostra a posição da primeira ocorrência do elemento
del(lanche) --> apaga todos os elementos da tupla


072: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso

073: Crie uma tupla preenchida com os 20 primeiros colocados da tabela da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados
B) Os últimos 4 colocados da tabela
C) Uma lista com os times em ordem alfabética
D) Em que posição na tabela está o time da Chapecoense

074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla

075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9
B) Em que posição foi digitado o primeiro valor 3
C) Quais foram os números pares

076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência
No final, mostre uma listagem de preços, organizando os dados em forma tabular
Ex: 
========================
LISTAGEM DE PREÇOS
========================
Lápis............R$ 1.75
Borracha.........R$ 2.00

077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''