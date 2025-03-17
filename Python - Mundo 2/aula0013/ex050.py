'''
050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o
'''
soma = 0
lista = []
for c in range(1, 7):
    num = int(input(f"Digite o {c}º número inteiro: "))
    if num % 2 == 0:
        soma += num
        lista.append(num)

print(f"O resultado da soma dos número pares {lista} foi de: {soma}")
