'''
086: CRIE UM PROGRAMA QUE CRIE UMA MATRIZ DE DIMENSÃO 3X3 E PREENCHA COM VALORES LIDOS PELO TECLADO
NO FINAL, MOSTRE A MATRIZ NA TELA, COM A FORMATAÇÃO CORRETA
EX:
1  2  3
4  5  6
7  8  8
'''

matriz = [[], [], []]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input((f'Adicione o elementro da {l+1}ª linha, e {c+1}ª coluna: '))))

for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end=' ')
    print()
