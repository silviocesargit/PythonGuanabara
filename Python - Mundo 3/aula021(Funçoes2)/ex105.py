'''
105: FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO NOTAS() QUE PODE RECEBER VÁRIAS NOTAS DE ALUNOS E VAI RETORNAR UM DICIONÁRIO COM AS SEGUINTES INFORMAÇÕES:
- QUANTIDADE DE NOTAS
- A MAIOR NOTA
- A MENOR NOTA
- A MÉDIA DA TURMA
- A SITUAÇÃO (OPCIONAL)

ADICIONE TAMBÉM AS DOCSTRINGS DA FUNÇÃO
'''


def notas(*n, sit=False):
    dic = {}
    maior = menor = 0
    soma = 0
    cont = 0
    situacao = ''
    for pos, nota in enumerate(n):
        cont += 1
        soma += nota
        if pos == 0:
            maior = nota
            menor = nota
        else:
            if nota > maior:
                maior = nota
            elif nota < menor:
                menor = nota
    media = soma / len(n)
    dic['total'] = cont
    dic['maior'] = maior
    dic['menor'] = menor
    dic['media'] = media
    if sit == False:
        return dic
    if media >= 7:
        situacao = 'Ótima'
    elif 7 > media >= 6:
        situacao = 'Boa'
    elif media < 6:
        situacao = 'Ruim'
    dic['situação'] = situacao
    if sit == True:
        return dic
        

resp = notas(5.5, 2.5, 1.5, sit=False)
print(resp)