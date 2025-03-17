'''
061: REFAÇA O DESAFIO 051, LENDO O PRIMEIRO TERMO E A RAZÃO DE UMA PA, MOSTRANDO OS 10 PRIMEIROS TERMOS DA PROGRESSÃO USANDO A ESTRUTURA WHILE
'''

primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
termos = primeiro_termo
cont = 9
print(f"Os 10 primeiros termos desta PA são: {termos}", end=' ')

while cont > 0:
    termos += razao
    print(termos, end=' ')
    cont -= 1