'''
087: APRIMORE O DESAFIO ANTERIOR, MOSTRANDO NO FINAL:
A) A SOMA DE TODOS OS VALORES PARES DIGITADOS
B) A SOMA DOS VALORES DA TERCEIRA COLUNA
C) O MAIOR VALOR DA SEGUNDA LINHA
'''
cont_par = 0
maior = 0
soma = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        elemento = int(input((f'Adicione o elementro da {l+1}ª linha, e {c+1}ª coluna: ')))
        matriz[l][c] = elemento
        if elemento % 2 == 0:
            cont_par += elemento
        if matriz[l][c] == matriz[l][2]:
            soma += matriz[l][c]
        if matriz[l][c] == matriz[1][0]:
            maior = matriz[l][c]
        else:
            if matriz[1][c] > maior:
                maior = matriz[l][c]


for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end=' ')
    print()

print()
print(f'A) A soma de todos os valores pares digitados: {cont_par}')
print(f'B) A soma dos valores da terceira coluna: {soma}')
print(f'O maior valor da segunda linha: {maior}')


