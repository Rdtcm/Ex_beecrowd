#Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.
dados = []
for i in range(100):
    num = int(input())
    dados.append(num)


maior_num = dados[0]
posicao = 0
for j in range(1,100):
    if dados[j] > maior_num:
        maior_num = dados[j]
        posicao = j

print(maior_num)
print(posicao)