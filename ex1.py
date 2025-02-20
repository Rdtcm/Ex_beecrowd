
num_linhas = int(input())

dados = []

for i in range(num_linhas):
    dados.append(input())


# ===== CRIPTOGRAFANDO =====
dados_criptografado = []

primeira_passada = ""
segunda_passada = ""
terceira_passada = ""

for msg in dados:
    #primeira passada
    for l in msg: 
        if l.isalpha():
            primeira_passada += chr(ord(l) + 3)
        else:
            primeira_passada += l
    #segunda passada
    segunda_passada = primeira_passada[::-1]
    #terceira passada
    metade = len(segunda_passada) // 2
    terceira_passada = segunda_passada[:metade]
    for c in segunda_passada[metade:]:
        terceira_passada += chr(ord(c) - 1)
    
    dados_criptografado.append(terceira_passada)

for mensagem in dados_criptografado:
    print(mensagem)

