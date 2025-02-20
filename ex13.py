num = input("Digite um numero:")

try:
    num = int(num)
    if num % 2 == 0:
        print("O numero e par")
    else:
        print("O numero e impar")
except:
    print("O numero nao einteiro")