#BEECROWD 1253 - CIFRA DE CESAR 

def main():
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    testes = int(input().strip())

    for i in range(testes):
        msg = input().strip().upper()
        num_desloc = int(input().strip())
        msg_criptada = ""
        for letra in msg:
            if letra in alfabeto:
                indice_original = alfabeto.index(letra)
                indice_novo = (indice_original - num_desloc) % 26
                msg_criptada += alfabeto[indice_novo]
            else:
                msg_criptada += letra
        
        print(msg_criptada)



if __name__ == '__main__':
    main()