'''
090: FAÇA UM PROGRAMA QUE LEIA NOME E MÉDIA DE UM ALUNO, GUARDANDO TAMBÉM A SITUAÇÃO EM UM DICIONÁRIO. NO FINAL, MOSTRE O CONTEÚDO DA ESTRUTURA NA TELA
'''

boletim = {}

boletim['nome'] = input('Nome: ')
boletim['media'] = float(input(f"Média de {boletim['nome']}: "))

if boletim['media'] >= 6:
    boletim['situacao'] = 'Aprovado'
else:
    boletim['situacao'] = 'Reprovado'
print('-='*30)
print(f"--- Nome é igual a {boletim['nome']}")
print(f"--- Média é igual a {boletim['media']}")
print(f"--- Situação é igual a {boletim['situacao']}")