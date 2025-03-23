def cadastro(nome="", idade=0):
    with open("cadastro.txt", "a") as cadastro:
        cadastro.write(f"Nome: {nome.ljust(20)} Idade: {idade}\n")