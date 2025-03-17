'''
082: CRIE UM PROGRAMA QUE VAI LER VÁRIOS NÚMEROS E COLOCAR EM UMA LISTA
DEPOIS DISSO, CRIE DUAS LISTAS EXTRAS QUE VÃO CONTER APENAS OS VALORES PARES E OS VALORES ÍMPARES DIGITADOS, RESPECTIVAMENTE
AO FINAL, MOSTRE O CONTEÚDO DAS TRÊS LISTAS GERADAS
'''

lista = []
listapar = []
listaimpar = []

while True:
    numero = int(input("Digite um número: "))
    lista.append(numero)
    if numero % 2 == 0:
        listapar.append(numero)
    else:
        listaimpar.append(numero)
    opcao = int(input("Digite (1) para continuar, ou (2) para parar: "))
    if opcao == 2:
        break

print()
print(lista)
print(listapar)
print(listaimpar)