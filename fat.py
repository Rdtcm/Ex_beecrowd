#fatorial com recursao

def fat(num):
    if num == 0:
        return 1
    else:
        return num * fat(num-1)
    
def main():
    num = int(input("Digite um numero: "))
    fatorial = fat(num)
    print(f"Fatorial de {num}: {fatorial}")

if __name__ == '__main__':
    main() 

