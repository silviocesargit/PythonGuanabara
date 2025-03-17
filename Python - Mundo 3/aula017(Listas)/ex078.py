'''
078: FAÇA UM PROGRAMA QUE LEIA 5 VALORES NUMÉRICOS E GUARDE-OS EM UMA LISTA
NO FINAL, MOSTRE QUAL FOI O MAIOR E O MENOR VALOR DIGITADO E AS SUAS RESPECTIVAS POSIÇÕES NA LISTA
'''
lista = []

for c in range(1, 6):
    lista.append(int(input(f'Digite o {c}º número: ')))

for c in range(0, len(lista)):
    if lista[c] == max(lista):
        print(f'O maior valor foi {max(lista)} na posição {c}')
    if lista[c] == min(lista):
        print(f'O menor valor foi {min(lista)} na posição {c}')