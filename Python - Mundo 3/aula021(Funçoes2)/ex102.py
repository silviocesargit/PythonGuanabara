'''
102: CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO FATORIAL() QUE RECEBA DOIS PARÂMETROS: O PRIMEIRO QUE INDIQUE O NÚMERO A CALCULAR E O OUTRO CHAMADO SHOW, QUE SERÁ UM VALOR LÓGICO (OPCIONAL) INDICANDO SE SERÁ MOSTRADO OU NÃO NA TELA O PROCESSO DE CÁLCULO DO FATORIAL
'''

def fatorial(n, show=0):
    """
    fatorial(n, show=False)
        -> Calcula o Fatorial de um número
        :param n: O número a ser calculado
        :param show: (opcional) Mostrar ou não a conta
        :return: O valor do Fatorial de um número n.
    """
    print("-"*30)
    resp = n
    if show == True:
        print(f'{resp} X', end=' ')
        for c in range(n - 1, 0, -1):
            print(f"{c} X ", end='')
            resp *= c
            if c == 1:
                print(f'{c} = {resp}')
        
    elif show == False:
        for c in range(n - 1, 0, -1):
            resp *= c
        print(resp)
help(fatorial)


