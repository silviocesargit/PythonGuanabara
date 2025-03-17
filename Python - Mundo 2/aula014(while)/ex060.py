'''
060: FAÇA UM PROGRAMA QUE LEIA UM NÚMERO QUALQUER E MOSTRE O SEU FATORIAL
EX: 5! = 5X4X3X2X1 = 120
'''

num = int(input("Digite um número para saber o seu fatorial: "))
cont = num
total = num
print()
print(f"{num}! = ", end='')
while cont > 0:
    print(f"{cont}x", end='')
    cont -= 1
    total *= cont
    if cont == 1:
        print(f"{cont} = ", end='')
        cont -= 1
    
print(total)
