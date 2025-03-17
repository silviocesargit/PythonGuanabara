'''
073: Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados
B) Os últimos 4 colocados da tabela
C) Uma lista com os times em ordem alfabética
D) Em que posição na tabela está o time da Chapecoense
'''
times = ("Flamengo", "Internacional", "Atlético Mineiro", "São Paulo", "Fluminense", "Grêmio", "Palmeiras", "Santos", "Athletico Paranaense", "Red Bull Bragantino", "Ceará", "Corinthians", "Atlético Goianiense", "Bahia", "Sport Recife", "Fortaleza", "Vasco da Gama", "Goiás", "Chapecoense", "Botafogo")
print()
print(f"* Os primeiros 5 colocados do Campeonato Brasileiro são:")
print()
for c in range(0, len(times)):
    if c < 5:
        print(f"{c+1}º - {times[c]}")
print()
print(f"* O últimos 4 colocados do Campeonato Brasileiro são:")
print()
for n in range(0, len(times)):
    if n > 15:
        print(f"{n+1}º - {times[n]}")
print()
for pos, team in enumerate(times):
    if 'Chapecoense' in team:
        print(f"* A posição do time da Chapecoense no Campeonato é a: {pos + 1}ª!")
print()
times_ordenados = sorted(times)
print("* A lista dos times do Campeonato ordenada em ordem alfabética é: ")
for time in times_ordenados:
    print(time, end=' - ')