'''
051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão
'''

num = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
print()
print("Os 10 primeiros termos da PA são: ", end='')

for c in range(1, 11):
    num += razao
    print(num, end=' ')
