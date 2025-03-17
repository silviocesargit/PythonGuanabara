'''
085: CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR SETE VALORES NUMÉRICOS E CADASTRE-OS EM UMA LISTA ÚNICA QUE MANTENHA SEPARADOS OS VALORES PARES E ÍMPARES. NO FINAL, MOSTRE OS VALORES PARES E ÍMPARES EM ORDEM CRESCENTE.
'''

lista = [[], []]

for c in range(0, 7):
    numero = int(input(f"Digite o {c+1}º valor: "))
    if numero % 2 == 0:
        lista[0].insert(0, numero)
    else:
        lista[1].insert(1, numero)
lista[0].sort()
lista[1].sort()
print(lista)