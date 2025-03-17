'''
089: CRIE UM PROGRAMA QUE LEIA NOME E DUAS NOTAS DE VÁRIOS ALUNOS E GUARDE TUDO EM UM LISTA COMPOSTA. NO FINAL, MOSTRE UM BOLETIM CONTENDO A MÉDIA DE CADA UM E PERMITA QUE O USUÁRIO POSSA MOSTRAR AS NOTAS DE CADA ALUNO INDIVIDUALMENTE
'''

lista_principal = []
temporaria = []

while True:
    nome = input("Digite o nome do aluno: ").upper()
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    temporaria.append(nome)
    temporaria.append(nota1)
    temporaria.append(nota2)
    lista_principal.append(temporaria[:])
    temporaria.clear()
    opcao = input("Deseja continuar [S/N]? ").upper()
    if 'N' in opcao:
        break

for p in lista_principal:
    media = (p[1]+p[2])/2
    print(f"A média de {p[0]} é igual a: {media}")

notas = input("Deseja visualizar as notas inviduais de algum aluno [S/N]? ").upper()
if 'S' in notas:
    aluno = input("Digite o nome do aluno que deseja buscar: ").upper()
    for a in lista_principal:
        if aluno == p[0]:
            print(f"As notas de {aluno} foram {p[1]} e {p[2]} respectivamente")


