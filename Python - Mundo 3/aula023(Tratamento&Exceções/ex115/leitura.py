def leitura():

    try:
        with open("cadastro.txt", "r") as cadastro:
            conteudo = cadastro.readlines()
            if conteudo == 0:
                print("Nenhuma pessoa cadastrada!")
            else:
                print("-"*40)
                print("PESSOAS CADASTRADAS".center(40))
                print("-"*40)
                for linha in conteudo:
                    print(linha.strip())
    except FileNotFoundError:
        print("Arquivo de cadastros não encontrado!")