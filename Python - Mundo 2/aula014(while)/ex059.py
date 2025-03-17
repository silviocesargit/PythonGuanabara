'''
059: CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU NA TELA:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
SEU PROGRAMA DEVERÁ REALIZAR A OPERAÇÃO SOLICITADA EM CADA CASO.
'''
import time

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print('''
Escolha a operação que deseja realizar com os números informados!
      
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
''')
print()
opcao = int(input("Digite a opção desejada: "))

while opcao != 5:

    if opcao == 1:
        print(f"{num1} + {num2} = {num1 + num2}")
        print()    
    elif opcao == 2:
        print(f"{num1} x {num2} = {num1 * num2}")
        print()
    elif opcao == 3:
        if num1 > num2:
            print(f"O maior entre os números digitados é o {num1}")
        else:
            print(f"O maior entre os números digitados é o {num2}")
        print()
    elif opcao == 4:
        num1 = int(input("Digite o primeiro número novamente: "))
        num2 = int(input("Digite o segundo número novamente: "))
        print()
    else:
        print("Opção inválida, escolha uma opção novamente!")

    time.sleep(2)

    print()

    print('''
Escolha a operação que deseja realizar com os números informado!
      
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
''')

    opcao = int(input("Digite a opção desejada: "))

time.sleep(2)
print("Obrigado por vir, até logo!")