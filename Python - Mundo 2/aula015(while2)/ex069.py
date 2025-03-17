'''
069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados
C) quantas mulheres tem menos de 20 anos
'''

maior_idade = 0
homens = 0
mulheres_menor20 = 0

while True:
    idade = int(input("Digite a sua idade: "))
    sexo = input("Digite o seu sexo [M/F]: ").upper()

    if idade >= 18:
        maior_idade += 1
    if 'M' in sexo:
        homens += 1
    if  'F' in sexo and idade < 20:
        mulheres_menor20 += 1
    
    opcao = input("Deseja continuar [S/N]: ").upper()

    if 'N' in opcao:
        break
print()
print(f"O total de pessoas maiores de idade cadastradas foi: {maior_idade}")
print(f"O total de homens cadastrados foi: {homens}")
print(f"O total de mulheres menores de 20 cadastradas foi: {mulheres_menor20}")
