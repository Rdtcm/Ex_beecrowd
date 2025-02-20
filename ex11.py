#Beecrowd  3301

h,z,l = [int(x) for x in input().split()]

dicionario = { 
    'h': h,
    'z': z,
    'l': l
}

maior = max(dicionario.values())
menor = min(dicionario.values())

for chave,valor in dicionario.items():
    if valor > menor and valor < maior:
        sobrinho = chave
    
if sobrinho == 'h':
    sobrinho = "huguinho"
elif sobrinho == 'l':
    sobrinho = "luisinho"
elif sobrinho == 'z':
    sobrinho = "zezinho"

print(sobrinho)


