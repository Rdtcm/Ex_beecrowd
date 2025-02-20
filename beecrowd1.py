# Leia um valor inteiro entre 1 e 12, inclusive. 
# Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso, em inglês, com a primeira letra maiúscula.

def obter_chave(dicionario, valor):
    for chave, val_dicionario in dicionario.items():
        if val_dicionario[0] == valor:
            return chave
        
tabela = {
    'January': [1],
    'February': [2],
    'March': [3],
    'April': [4],
    'May': [5],
    'June': [6],
    'July': [7],
    'August': [8],
    'September': [9],
    'October': [10],
    'November': [11],
    'December': [12],
}

number = int(input())
if (1<=number<=12):
    mes = obter_chave(tabela, number)
    print(mes)