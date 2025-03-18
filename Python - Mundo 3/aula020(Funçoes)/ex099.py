'''
099: FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA MAIOR(), QUE RECEBA VÁRIOS PARÂMETROS COM VALORES INTEIROS.
SEU PROGRAMA TEM QUE ANALISAR TODOS OS VALORES E DIZER QUAL DELES É O MAIOR
'''

def maior(*num):
    maior = 0
    
    for c in num:
        if c == num[0]:
            maior = c
        elif c > maior:
            maior = c
    
    print(f"Os elementos foram {num} e o maior é {maior}")

maior(1, 9, 4, 3, 7)
