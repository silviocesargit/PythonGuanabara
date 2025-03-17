'''
049: Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for
'''
num = int(input("Digite um número para saber a sua tabuada: "))
print()
print(f"Esta é a tabuado do número {num}: ")
for c in range(1, 10):
    print(f"{c} + {num} = {c + num}")
for c in range(1, 10):
    print(f"{c} - {num} = {c - num}")
for c in range(1, 10):
    print(f"{c} x {num} = {c * num}")
for c in range(1, 10):
    print(f"{c} / {num} = {c / num}")