'''
LISTA (1)

Exemplo de parâmetro

def texto(txt):
    print("--------------------------------")
    print(txt)
    print("--------------------------------")

texto("Curso em Vídeo")

Outro exemplo

def soma(a, b):
    s = a + b

soma(4, 5) --> Ele vai realizar a operação que está dentro da função declarada, utilizando os parâmetros definidos

EMPACOTAMENTO (Quando se tem vários parâmetros declarados na hora de chamar a função e você separa(desempacota) eles)

ex:
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(2, 9, 4)

def contador(*num): --> Essa nomeclatura significa que serão passados vários elementos para o parâmetro e todos serão enviados para "num"
    print(num)

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

Com base nessas operações, a Função irá criar uma tupla com os números informados em cada uma das chamadas

Conclui-se que pode realizar qualquer operação dentro da função que também possa ser realizado dentro de uma tupla

PODE-SE PASSAR UMA LISTA PARA O PARÂMETRO DA FUNÇÃO!

def dobra(lst):
    pos = 0
    while pos < len(lst):
    lst[pos] *= 2
    pos += 1

valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)

DESAFIOS:

096: FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA ÁREA(), QUE RECEBA AS DIMENSÕES DE UM TERRENO RETANGULAR (LARGURA E COMPRIMENTO) E MOSTRE A ÁREA DO TERRENO

097: FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMA ESCREVE(), QUE RECEBA UM TEXTO QUALQUER COMO PARÂMETRO E MOSTRE UMA MENSAGEM COM TAMANHO ADAPTÁVEL
EX:
ESCREVA('OLÁ, MUNDO!')
SAÍDA:
-----------------
OLÁ, MUNDO!
-----------------

098: FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA CONTADOR(), QUE RECEBA TRÊS PARÂMETROS: INÍCIO, FIMM E PASSO E REALIZE A CONTAGEM

SEU PROGRAMA TEM QUE REALIZAR TRÊS CONTAGENS ATRAVÉS DA FUNÇÃO CRIADA:
A) DE 1 ATÉ 10, DE 1 EM 1
B) DE 10 ATÉ 0, DE 2 EM 2
C) UMA CONTAGEM PERSONALIZADA

099: FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA MAIOR(), QUE RECEBA VÁRIOS PARÂMETROS COM VALORES INTEIROS.
SEU PROGRAMA TEM QUE ANALISAR TODOS OS VALORES E DIZER QUAL DELES É O MAIOR

100: FAÇA IM PROGRAMA QUE TENHA UMA LISTA CHAMADA NÚMEROS E DUAS FUNÇÕES CHAMADAS SORTEIA() E SOMAPAR(). A PRIMEIRA FUNÇÃO VAI SORTEAR 5 NÚMEROS E VAI COLOCÁ-LOS DENTRO DA LISTA E A SEGUNDA FUNÇÃO VAI MOSTRAR A SOMA ENTRE TODOS OS VALORES PARES SORTEADOS PELA FUNÇÃO ANTERIOR.


'''