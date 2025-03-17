'''
079: CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR VÁRIOS VALORES NUMÉRICOS E CADASTRE-OS EM UMA LISTA. CASO O NÚMERO JÁ EXISTA LÁ DENTRO, ELE NÃO SERÁ ADICIONADO. NO FINAL, SERÃO EXIBIDOS TODOS OS VALORES ÚNICOS DIGITADOS, EM ORDEM CRESCENTE.
'''

lista = []

while True:
    numero = int(input("Digite um númemro para adicionar a lista: "))
    if numero not in lista:
        lista.append(numero)
    opcao = input("Deseja adicionar mais algum número [S/N]: ").upper()
    if 'N' in opcao:
        break
lista.sort()
print(f'O valores digitados em ordem crescente foram: {lista}')
 