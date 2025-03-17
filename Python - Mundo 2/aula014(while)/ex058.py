'''
058: MELHORE O DESAFIO 028 ONDE O COMPUTADOR VAI "PENSAR" EM UM NÚMERO ENTRE 0 E 10. SÓ QUE AGORA O JOGADOR VAI TENTAR ADIVINHAR ATÉ ACERTAR, MOSTRANDO NO FINAL QUANTOS PALPITES FORAM NECESSÁRIOS PARA VENCER.
'''
import random

cont = 0
numero_aleatorio = random.randint(0, 10)
print(numero_aleatorio)
print()
palpite = int(input("Digite o seu palpite (Escolha de 0 a 10): "))
cont += 1
while palpite != numero_aleatorio:
    print("Você errou! Tente novamente...")
    cont += 1
    palpite = int(input("Digite o seu palpite (Escolha de 0 a 10): "))

print(f"Você acertou! Total de {cont} palpites. O número sorteado foi o {numero_aleatorio}")
