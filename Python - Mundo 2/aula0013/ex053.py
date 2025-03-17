'''
053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços
ex: apos a sopa, a sacada da casa, a torre da derrota, o lobo ama o bolo
'''

frase = input("Digite uma frase para saber se é um PALÍNDROMO: ").lower().split()
frase_SemEspaco = ''.join(frase)
frase_Invertida = frase_SemEspaco[::-1]

if frase_SemEspaco == frase_Invertida:
    print(f"{frase_SemEspaco} é um PALÍNDROMO")
else:
    print(f"O inverso de {frase_SemEspaco} é {frase_Invertida}, logo não é um PALÍNDROMO")

