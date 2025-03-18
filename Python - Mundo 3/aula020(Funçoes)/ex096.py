'''
096: FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA ÁREA(), QUE RECEBA AS DIMENSÕES DE UM TERRENO RETANGULAR (LARGURA E COMPRIMENTO) E MOSTRE A ÁREA DO TERRENO
'''

def area():

    a = int(input("Altura: "))
    b = int(input("Largura: "))
    area = a*b
    print(f"A área do retângulo é: {area}")

area()