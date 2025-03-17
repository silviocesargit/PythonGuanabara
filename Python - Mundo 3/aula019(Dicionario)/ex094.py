'''
094: CRIE UM PROGRAMA QUE LEIA NOME, SEXO E IDADE DE VÁRIAS PESSOAS, GUARDANDO OS DADOS DE CADA PESSOA EM UM DICIONÁRIO E TODOS OS DICIONÁRIOS EM UMA LISTA. NO FINAL, MOSTRE:
A) QUANTAS PESSOAS FORAM CADASTRADAS
B) A MÉDIA DE IDADE DO GRUPO
C) UMA LISTA COM MULHERES
D) UMA LISTA COM TODAS AS PESSOAS COM IDADE ACIMA DA MÉDIA
'''

dados = {}
listagem = []
listagem_mulheres = []
listagem_acima = []
media_grupo = 0

while True:
    dados['nome'] = input("Nome: ")
    dados['sexo'] = input("Sexo [M/F]: ").upper()
    while dados['sexo'] not in 'MF':
        print("ERRO! Por favor, digite apenas M ou F.")
        dados['sexo'] = input("Sexo [M/F]: ").upper()
    dados['idade'] = int(input("Idade: "))
    media_grupo += dados['idade']
    listagem.append(dados.copy())
    if dados['sexo'] in 'F':
        listagem_mulheres.append(dados['nome'])
    opcao = input("Deseja continuar [S/N]: ").upper()
    while opcao not in 'SN':
        print("ERRO! Responda apenas S ou N.") 
        opcao = input("Deseja continuar [S/N]: ").upper()  
    if 'N' in opcao:
        break
print("-="*35)
print(f"Ao todo temos {len(listagem)} pessoas cadastradas.")
print(f"B) A média de idade é de {media_grupo / len(listagem)}")
print(f"C) As mulheres cadastradas foram: ", end='')
for po, m in enumerate(listagem_mulheres):
    if po == (len(listagem_mulheres) - 1):
        print(m)
    else:
        print(m, end=' ')
print("D) Lista de pessoas que estão acima da média: ")
for pos, p in enumerate(listagem):
    if p['idade'] > media_grupo / len(listagem):
        print(f"     nome = {p['nome']}; sexo = {p['sexo']}; idade = {p['idade']}")
    

