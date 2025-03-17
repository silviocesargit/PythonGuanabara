'''
063: ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO N INTEIRO QUALQUER E MOSTRE NA TELA OS N PRIMEIROS ELEMENTOS DE UMA SEQUÊNCIA DE FIBONACCI
EX: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> -> 8
'''


num = int(input("Digite o número de termos para saber sua Sequência de Fibonacci: "))
t1 = 0
t2 = 1

cont = 3

print(f"{t1} -> {t2}", end='')

while cont <= num:
    t3 = t1 + t2    
    print(f" -> {t3}",  end='')
    t1 = t2
    t2 = t3
    cont += 1