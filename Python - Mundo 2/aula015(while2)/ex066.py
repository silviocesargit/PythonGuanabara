'''
066: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)
'''
cont = 0
soma = 0
while True:
    num = int(input("Digite um número inteiro: "))
    if num == 999:
        break
    cont += 1
    soma += num
print()
print(f"O número total de números digitados foi de {cont}, a soma deles foi {soma}")
