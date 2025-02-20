#inverter uma string
def main():
    string = input("Digite uma string: ")

    new_str = string[::-1]

    print(f"String invertida: {new_str}")


if __name__ == '__main__':
    main()