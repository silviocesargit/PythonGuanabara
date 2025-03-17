'''
062: MELHORE O DESAFIO 061, PERGUNTANDO PARA O USUÁRIO SE ELE QUER MOSTRAR MAIS ALGUNS TERMOS. O PROGRAMA ENCERRA QUANDO ELE DISSER QUE QUER MOSTRAR 0 TERMOS
'''

primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
termos = primeiro_termo
cont = 9
opcao = 1
print(f"Os 10 primeiros termos desta PA são: {termos}", end=' ')


while opcao != 0:

    while cont > 0:
        termos += razao
        print(termos, end=' ')
        cont -= 1
    print()
    opcao = int(input("Deseja mostrar mais algum termo? Digite o número de termos: "))
    if opcao > 0:
        cont = opcao
        while cont > 0:
            termos += razao
            print(termos, end=' ')
            cont -= 1
        print()