'''
023 -> FAÇA UM PROGRAMA QUE LEIA UM NÚMERO DE 0 A 9999 E MOSTRE NA TELA CADA UM DOS DÍGITOS SEPARADOS.
EX:
DIGITE UM NÚMERO: 1834

UNIDADE: 4
DEZENA: 3
CENTENA: 8
MILHAR: 1
'''

num = (input("Digite um numero de 0 a 9999: "))
num = num[::-1]
print(f'UNIDADE: {num[0]}')
print(f'DEZENA: {num[1]}')
print(f'CENTENA: {num[2]}')
print(f'MILHAR: {num[3]}')
