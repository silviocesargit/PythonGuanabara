'''
098: FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA CONTADOR(), QUE RECEBA TRÊS PARÂMETROS: INÍCIO, FIMM E PASSO E REALIZE A CONTAGEM

SEU PROGRAMA TEM QUE REALIZAR TRÊS CONTAGENS ATRAVÉS DA FUNÇÃO CRIADA:
A) DE 1 ATÉ 10, DE 1 EM 1
B) DE 10 ATÉ 0, DE 2 EM 2
C) UMA CONTAGEM PERSONALIZADA
'''
from time import sleep

def contador(i, f, p):
    print("-="*20)
    print(f"Contagem de {i} até {f} de {p} em {p}")
    cont = i
    if i < f:
        while cont < f:
            print(f"{cont}", end=' ', flush=True)
            cont += p
            sleep(0.5)
    if i > f:
        while cont > f:
            print(f"{cont}", end=' ', flush=True)
            cont -= p
            sleep(0.5)
    print("FIM!")

contador(1, 10, 1)
contador(10, -1, 2)
print("-="*20)
print(f"Agora é sua vez de personalizar a contagem!")
i = int(input("Início: "))
f = int(input("Fim:    "))
p = int(input("Passo:  "))
contador(i, f, p)

