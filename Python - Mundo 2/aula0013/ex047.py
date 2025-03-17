'''
047: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50
'''
print("No intervalo entre 1 e 50, são números pares: ")
for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=' ')
