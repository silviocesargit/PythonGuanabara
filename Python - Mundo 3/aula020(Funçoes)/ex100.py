'''
100: FAÇA UM PROGRAMA QUE TENHA UMA LISTA CHAMADA NÚMEROS E DUAS FUNÇÕES CHAMADAS SORTEIA() E SOMAPAR(). A PRIMEIRA FUNÇÃO VAI SORTEAR 5 NÚMEROS E VAI COLOCÁ-LOS DENTRO DA LISTA E A SEGUNDA FUNÇÃO VAI MOSTRAR A SOMA ENTRE TODOS OS VALORES PARES SORTEADOS PELA FUNÇÃO ANTERIOR.
'''

def sorteia(lst):
    from random import randint
    for c in range(0, 5):
        lst.append(randint(1, 20))
    print(f"A lista sorteada foi: {lst}")

def somapar(lst):
    soma = 0
    for n in lst:
        if n % 2 == 0:
            soma += n
    print(f"A soma dos números pares de {lst} é igual a {soma}")

lista = []
sorteia(lista)
somapar(lista)
