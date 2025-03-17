'''
frase = 'Curso em Vídeo Python'

Cada uma das letras e espaços, recebem um índice, começando a partir do 0

* FATIAMENTO (Técnica para pegar pedaços de uma string)

frase[9] --> Ele vai buscar o caractere de índice 9

frase[9:13] --> Ele vai buscar os caracteres do indice 9 até o 12, no final é um contado um número a menos

frase[9:21:2] --> Ele vai do indice 9 até o 20, pulando de 2 em 2 caracteres. Exemplo ele vai mostrar o V d o P t o

frase[:5] --> quando eu omito o início do fatiamente, ele busca do início da string

frase[15:] --> quando eu omito o final, ele busca até o final da string

frase[9::3] --> Ele vai buscar do índice 9 e vai até o final, pulando de 3 em 3 strings

* ANÁLISE (Técnica para analisar uma string)

len(frase) --> mostra o comprimento da string, ou seja a soma dos índices ocupados pela string

frase.count('o') --> o count serve para contar quantas vezes a string especificada aparece na string

frase.count('o', 0, 13) --> vai contar quantas vezes a string especificada aparece dentro do intervalo do índice 0 até o 12

frase.find('deo') --> vai mostrar a posição (considerando a primeira posição que a string surge) que a string especificada aparece dentro da string da variável

    obs.: Se você tentar encontrar a posição de alguma string específica através do find e essa string não existir, ele vai retornar -1

'Curso' in frase --> Se existir ele vai retornar True, caso contrário, False

*TRANSFORMAÇÃO (Métodos para alterar uma string dentro de uma variável)

frase.replace('Python', 'Android') --> Ele vai buscar a string Python e substituir por Android

frase.upper() --> Torna todas as letras da string em maiúsculo

frase.lower() --> Torna todas as letras da string em minúsculo

frase.capitalize() --> Joga todas as letras da string para minúsculo, com exceção da primeira

frase.title() --> Vai jogar todas as primeiras letras das palavras em maíusculo, e as demais ficarão em minúsculo

ex: frase =    Aprenda Python  

frase.strip() --> Vai remover todos os espaços inúteis no começo e no final da string

frase.rstrip() --> r de right serve para tirar os espaços da direita

frase.lstrip() --> l de left serve para tirar os espaços da esquerda

* DIVISÃO (É possível dividir as strings)

frase.split() --> Ocorre uma divisão onde houver espaços na string, ou seja cada palavra separada por espaço receberá os índices de acordo com o seu tamanho, e logo após serão colocadas dentro de uma lista

* JUNÇÃO (É possível juntar)

'-'.join(frase) --> Serve para realizar o inverso do split, ou seja juntará todas as palavras para se tornar uma única string colocando o elemento entre aspas para os espaços que separam uma palavra uma da outra


EXERCÍCIOS:

022 -> CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE PESSOA E MOSTRE:
* O NOME COM TODAS AS LETRAS MAÍUSCULAS
* O NOME COM TODAS MINÚSCULAS
* QUANTAS LETRAS AO TODO (SEM CONSIDERAR OS ESPAÇOS)
* QUANTAS LETRAS TEM O PRIMEIRO NOME

023 -> FAÇA UM PROGRAMA QUE LEIA UM NÚMERO DE 0 A 9999 E MOSTRE NA TELA CADA UM DOS DÍGITOS SEPARADOS.
EX:
DIGITE UM NÚMERO: 1834

UNIDADE: 4
DEZENA: 3
CENTENA: 8
MILHAR: 1

024 -> CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA OU NÃO COM O NOME "SANTO"

025 -> CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA DIGA SE ELA TEM "SILVA" NO NOME

026 -> FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:
* QUANTAS VEZES APARECE A LETRA "A"
* EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ
* EM QUE POSIÇÃO ELA APARECE A ÚLTIMA VEZ

FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, MOSTRANDO EM SEGUIDA O PRIMEIRO E O ÚLTIMO NOME SEPARADAMENTE
EX: ANA MARIA DE SOUZA
PRIMEIRO = ANA
ÚLTIMO = SOUZA

'''