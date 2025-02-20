# beecrownd 1094

# tres tipos de cobais ; coelhos, ratos e sapos 
casos = []
n = int(input())  # numero de casos de teste

for l in range(n):
    linha = input().split(" ")
    numero = int(linha[0])
    text = linha[1]
    casos.append([numero,text])
# total de cobaias, coelhos, ratos e sapos
total_cobaias = 0
total_coelhos = 0
total_sapos = 0
total_ratos = 0
for i in range(n):
    total_cobaias += casos[i][0]
    if casos[i][1] == 'C' or casos[i][1] == 'c':
        total_coelhos += casos[i][0]
    elif casos[i][1] == 'R' or casos[i][1] == 'r':
        total_ratos += casos[i][0]
    elif casos[i][1] == 'S' or casos[i][1] == 's':
        total_sapos += casos[i][0]

percent_coelhos = (total_coelhos / total_cobaias) * 100
percent_ratos = (total_ratos / total_cobaias) * 100
percent_sapos = (total_sapos / total_cobaias) * 100

print(f"Total: {total_cobaias} cobaias")
print(f"Total de coelhos: {total_coelhos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de sapos: {total_sapos}")
print(f"Percentual de coelhos: {percent_coelhos:.2f} %")
print(f"Percentual de ratos: {percent_ratos:.2f} %")
print(f"Percentual de sapos: {percent_sapos:.2f} %")
