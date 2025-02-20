

def main():
    casos_teste = int(input().strip())
    for _ in range(casos_teste):
        msg = input().lower().strip()
        msg_tratada = ''.join([palavra[0] for palavra in msg.split()])
        print(msg_tratada)


if __name__ == '__main__':
    main()