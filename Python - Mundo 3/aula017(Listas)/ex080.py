'''
080: CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR CINCO VALORES NUMÉRICOS E CADASTRE-OS EM UMA LISTA, JÁ NA POSIÇÃO CORRETA DE INSERÇÃO (SEM USAR O SORT())
NO FINAL, MOSTRE A LISTA ORDENADA NA TELA
'''

lista = []


for c in range(0, 5):
    numero = int(input(f"Digite o {c+1}º número da lista: "))

    if len(lista) == 0 or numero > lista[-1]:
        lista.append(numero)
        print(f"Valor adicionado no final da lista")

    else:
        pos = 0
        while pos < len(lista):
            if numero < lista[pos]:
                lista.insert(pos, numero)
                print(f"Elemento adicionado na posição {pos}")
                break
            pos += 1
print()
print(f"A lista ordenada dos elementos é: {lista}")