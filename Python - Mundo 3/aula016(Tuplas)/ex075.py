'''
075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9
B) Em que posição foi digitado o primeiro valor 3
C) Quais foram os números pares
'''

n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))
n3 = int(input("Digite o 3º número: "))
n4 = int(input("Digite o 4º número: "))

tupla = (n1, n2, n3, n4)
contador9 = tupla.count(9)
posicao3 = tupla.index(3)
print()
print(f"O número 9 apareceu {contador9} vezes")
print()
print(f"O número 3 teve sua primeira ocorrência na posição: {posicao3}")
print()
print(f"Os números pares digitados foram: ", end=' ')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')
print()