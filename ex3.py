# beecrowd 1865

n = int(input())

dados = []

for i in range(n):
    players = [str(x) for x in input().split()]
    dados.append(players)
    

for player in dados:
    if player[0] == "Thor":
        print("Y")
    else:
        print("N")
