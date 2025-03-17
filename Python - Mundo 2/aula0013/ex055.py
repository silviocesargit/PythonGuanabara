'''
055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''

maior = 0
menor = 0

for c in range(1, 2):
    peso = int(input(f"Digite o peso da {c}ª pessoa: "))
    maior = peso
    menor = peso
for c in range(2, 6):
    peso = int(input(f"Digite o peso da {c}ª pessoa: "))
    if peso > maior:
        maior = peso
    else:
        if peso < menor:
            menor = peso

print(f"O maior peso foi de {maior} e o menor foi de {menor}")