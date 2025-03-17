'''
067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''

while True:
    num = int(input("Digite um número para saber a sua tabuada: "))
    if num <= 0:
        break
    else:
        for c in range(1, 10):
            print(f'{c} + {num} = {c + num}', end="  ")
            print(f'{c} - {num} = {c - num}', end="  ")
            print(f'{c} x {num} = {c * num}', end="  ")
            print(f'{c} / {num} = {c / num}')
    print()