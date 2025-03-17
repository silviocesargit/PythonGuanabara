'''
081: CRIE UM PROGRAMA QUE VAI LER VÁRIOS NÚMEROS E COLOCAR EM UMA LISTA
DEPOIS DISSO, MOSTRE:
A) QUANTOS NÚMEROS FORAM DIGITADOS
B) A LISTA DE VALORES, ORDENADA DE FORMA DESCRESCENTE
C) SE O VALOR 5 FOI DIGITADO E ESTÁ OU NÃO NA LISTA
'''

lista = []
cont = 0

while True:
    lista.append(int(input("Digite um número: ")))
    cont += 1
    opcao = input('Deseja continuar [S/N]: ').upper()
    if 'N' in opcao:
        break

print()
print(f"O número total de elementos adicionados a lista foi de: {cont}")
print()
ordem_decrescente = lista.sort(reverse=True)
print(f'A lista ordenada de forma decrescente é: {ordem_decrescente}')
print(f"A lista normal é {lista}")
print()
if 5 in lista:
    print(" O valor 5 está na lista!")
else:
    print("O valor 5 não está na lista!")

