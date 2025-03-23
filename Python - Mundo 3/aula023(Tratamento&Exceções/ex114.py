'''
114: CRIE UM CÓDIGO EM PYTHON QUE TESTE SE O SITE PUDIM ESTÁ ACESSÍVEL PELO COMPUTADOR USADO
'''

import requests

try:
    response = requests.get("http://www.pudim.com.br")
    if response.status_code == 200:
        print("O site Pudim está acessível!")
    else:
        print(f"Erro ao acessar o site. Código: {response.status_code}")
except requests.ConnectionError:
    print("Não foi possível acessar o site.")


