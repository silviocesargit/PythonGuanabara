'''
092: CRIE UM PROGRAMA QUE LEIA NOME, ANO DE NASCIMENTO E CARTEIRA DE TRABALHO E CADASTRE-OS (COM IDADE) EM UM DICIONÁRIO SE POR ACASO A CTPS FOR DIFERENTE DE ZERO, O DICIONÁRIO RECEBERÁ TAMBÉM O ANO DE CONTRATAÇÃO E O SALÁRIO. CALCULE E ACRESCENTE, ALÉM DA IDADE, COM QUANTOS ANOS A PESSOA VAI SE APOSENTAR
'''
from datetime import datetime
dados = {}

dados['nome'] = input("Nome: ")
dados['nascimento'] = int(input("Ano de Nascimento: "))
dados['idade'] = datetime.now().year - dados['nascimento']
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário R$: '))
    dados['aposentadoria'] = (35 - (datetime.now().year - dados['contratacao'])) + dados['idade']
print('-='*30)
for k, v in dados.items():
    print(f"  - {k} tem valor {v}")
        
