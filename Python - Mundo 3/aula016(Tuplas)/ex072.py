'''
072: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso
'''

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input("Digite um número de 0 a 20, para saber sua escrita por extenso: "))
'''
for pos, n in enumerate(numeros):
    if pos == num:
        print(f"O número {num} por extenso é: {n}")
'''
for c in range(0, len(numeros)):
    if c == num:
        print(f"O número {num} por extenso é: {numeros[c]}")
