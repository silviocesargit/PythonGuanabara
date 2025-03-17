'''
022 -> CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE PESSOA E MOSTRE:
* O NOME COM TODAS AS LETRAS MAÍUSCULAS
* O NOME COM TODAS MINÚSCULAS
* QUANTAS LETRAS AO TODO (SEM CONSIDERAR OS ESPAÇOS)
* QUANTAS LETRAS TEM O PRIMEIRO NOME
'''

nome = input("Digite o seu nome completo: ")

print("O seu nome com letras maiúsculas é: ", nome.upper())
print("O seu nome com letras minúsculas é: ", nome.lower())
nome_semespaco = nome.split()
nome_semespaco = ''.join(nome_semespaco)
print(f'Quantidade total de letras, desconsiderando os espaços: {len(nome_semespaco)}')

