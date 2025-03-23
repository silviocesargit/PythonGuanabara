'''
TRATAMENTO DE ERROS E EXCEÇÕES:

PALAVRAS RESERVADAS -> TRY (Comando) / EXCEPCT (Se der errado) / ELSE (Se der certo) / FINALLY (Independente de dar certo ou errado)

No caso do ELSE e do FINALLY, são comandos opicionais dentro do TRY / EXCEPT

EXEMPLO:

try:
    a = int(input("Numerador: ))
    b = int(input("Denominador: ))
except:
    print("Infelizmente tivemos um problema! ")
else:
    print(f"O resultado é {r:1.f}")
finally:
    print("Volte sempre! Muito obrigado!")


Também há a possibilidade de printar o erro no comando except:

try:
    a = int(input("Numerador: ))
    b = int(input("Denominador: ))
except Exception as erro:
    print(f"Problema encontrado foi {erro.__class__} ")
else:
    print(f"O resultado é {r:1.f}")
finally:
    print("Volte sempre! Muito obrigado!")

UM ERRO DENTRO DO TRY, PODE TER VÁRIOS EXCEPT PARA MOSTRAR NA TELA OS ERROS DE ACORDO COM A CLASSE DO ERRO POR EXEMPLO

EXEMPLO:

try:
    a = int(input("Numerador: ))
    b = int(input("Denominador: ))
except (ValueError, TypeError):
    print("Tivemos um problema com os tipos de dados que você informou")
except ZeroDivisionError:
    print("Não é possível dividir um número por zero!")
exept KeyboardInterrupt:
    print("O usuário preferiu não informar os dados!")
else:
    print(f"O resultado é {r:1.f}")
finally:
    print("Volte sempre! Muito obrigado!")

DESAFIOS:

113: REESCREVA A FUNÇÃO leaiint() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade

114: CRIE UM CÓDIGO EM PYTHON QUE TESTE SE O SITE PUDIM ESTÁ ACESSÍVEL PELO COMPUTADOR USADO

115: CRIE UM PEQUENO SISTEMA MODULARIZADO QUE PERMITA CADASTRAR PESSOAS PELO SEU NOME E IDADE EM UM ARQUIVO DE TEXTO SIMPLES
O SISTEMA SÓ VAI TER 2 OPÇOES: CADASTRAR UMA NOVA PESSOA E LISTAR TODAS AS PESSOAS CADASTRADAS
'''