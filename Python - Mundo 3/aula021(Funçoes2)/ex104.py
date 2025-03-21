'''
104: CRIE UM PROGRAMA QUE TENHA A FUNÇÃO LEAINT(), QUE VAI FUNCIONAR DE FORMA SEMELHANTE À FUNÇÃO INPUT() DO PYTHON. SÓ QUE FAZENDO A VALIDAÇÃO PARA ACEITAR APENAS UM VALOR NUMÉRICO.
EX:
N = LEIAINT('DIGITE UM N')
'''

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("ERRO! Digite um número válido.")
        if ok:
            break
    return valor


n = leiaint("Digite um número: ")
print(f"Você digitou o {n}")