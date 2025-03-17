'''
084: FAÇA UM PROGRAMA QUE LEIA NOME E PESO DE VÁRIAS PESSOAS, GUARDANDP TUDO EM UMA LISTA. NO FINAL, MOSTRE:
A) QUANTAS PESSOAS FORAM CADASTRADAS
B) UMA LISTAGEM COM AS PESSOAS MAIS PESADAS
C) UMA LISTAGEM COM AS PESSOAS MAIS LEVES
'''


pessoas = []
lista = []
maior = menor = 0
listagem_maior = []
listagem_menor = []

while True:
    lista.append(input('Digite o nome: '))
    lista.append(float(input('Digite o peso: ')))
    pessoas.append(lista[:])
    lista.clear()
    opcao = input('Quer continuar [S/N]: ').upper()
    if 'N' in opcao:
        break
print()
print(f'* {len(pessoas)} pessoas foram cadastradas.')

for posi, p in enumerate(pessoas):
    if posi == 0:
        maior = p[1]
        menor = p[1]
    elif p[1] > maior:
        maior = p[1]
    elif p[1] < menor:
        menor = p[1]
pos = 0
while pos < len(pessoas):
    for po, pessoa in enumerate(pessoas):
        if po == pos and pessoa[1] == maior:
            listagem_maior.append(pessoa[0])
        elif po == pos and pessoa[1] == menor:
            listagem_menor.append(pessoa[0])
    pos += 1

print(f"O maior peso é {maior}, das pessoas {listagem_maior}")
print(f"O menor peso é {menor}, das pessoas {listagem_menor}")
print(pessoas)

