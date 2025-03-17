'''
057: FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA, MAS SÓ ACEITE OS VALORES 'M' OU 'F'. CASO ESTEJA ERRADO, PEÇA A DIGITAÇÃO NOVAMENTE ATE TER UM VALOR CORRETO
'''

sexo = input("Digite o seu sexo [M ou F]: ").upper()

while sexo not in 'MF':
    sexo = input("Digite o seu sexo [M ou F]: ").upper()

