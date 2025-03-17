'''
048: Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500
'''
soma = 0
print("A soma entre os números ímpares e múltiplos de 3 entre 1 e 500 é: ")

for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c

print(soma)