'''
113: REESCREVA A FUNÇÃO leaiint() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade
'''

def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print("ERRO! Digite um número inteiro válido.")
            continue
        except (KeyboardInterrupt):
            print("ERRO! Usuário preferiu não digitar esse número.")
            return 0
        else:
            return valor
def leiaFloat(msg):
    ok = False
    valor = 0
    while ok == False:
        try:
            valor = float(input(msg))
        except:
            print("ERRO! Digite um número real válido.")
        else:
            return valor

numI = leiaInt("Digite um Inteiro: ")
print(f"Você digitou o número inteiro {numI}")
numF = leiaFloat("Digite um Real: ")
print(f"Você digitou o número real {numF}")