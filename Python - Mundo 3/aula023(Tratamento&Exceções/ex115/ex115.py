'''
115: CRIE UM PEQUENO SISTEMA MODULARIZADO QUE PERMITA CADASTRAR PESSOAS PELO SEU NOME E IDADE EM UM ARQUIVO DE TEXTO SIMPLES
O SISTEMA SÓ VAI TER 2 OPÇOES: CADASTRAR UMA NOVA PESSOA E LISTAR TODAS AS PESSOAS CADASTRADAS
'''

import cadastro
import leitura

while True:
    print("-"*40)
    print("MENU PRINCIPAL".center(40))
    print("-"*40)
    print('''
1 - Ver pessoas cadastradas
2 - Cadastrar nova Pessoa
3 - Sair do Sistema
''')
    print("-"*40)
    while True:
        try:
            opcao = int(input("Sua Opção:  "))
        except ValueError:
            print("ERRO! Digite um número inteiro válido.")
        else:
            if opcao > 3:
                print("ERRO! Digite um número dentro das opções disponíveis.")
            elif opcao == 1 or opcao == 2 or opcao == 3:
                break
    if opcao == 1:
        leitura.leitura()
    elif opcao == 2:
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        print(f"Novo registro de {nome} adicionado.")
        cadastro.cadastro(nome, idade)
    elif opcao == 3:
        break


