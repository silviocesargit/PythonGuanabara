'''
071) Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
'''

cont50 = 0
cont20 = 0
cont10 = 0
cont1 = 0

saque = int(input("Digite um valor para saque: "))
print(f"  --> Para o valor de {saque}, serão: ")

while True:
    if saque >= 50:
        saque -= 50
        cont50 += 1
    elif saque >= 20:
        saque -= 20
        cont20 += 1
    elif saque >= 10:
        saque -= 10
        cont10 += 1
    elif saque >= 1:
        saque -= 1
        cont1 += 1
    elif saque == 0:
        break
print(f'''
  {cont50} cédulas de 50 reais
  {cont20} cédulas de 20 reais
  {cont10} cédulas de 10 reais
  {cont1} cédulas de 1 real
''')