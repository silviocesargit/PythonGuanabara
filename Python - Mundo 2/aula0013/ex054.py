'''
054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
'''
maiores = 0
menores = 0

for c in range(1, 8):
    ano_nascimento = int(input(f"Digite o ano de nascimento da {c}ª pessoa: "))
    if 2025 - ano_nascimento >= 18:
        maiores += 1
    else:
        menores += 1

print(f"O número total de maiores de idade é de {maiores}")
print(f"O número total de menores de idade é de {menores}")
