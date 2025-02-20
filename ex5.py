#BEECROWD 1957

def decimal_to_hex(decimal):
    if decimal == 0:
        return "0"
    
    hex_dig = "0123456789ABCDEF"
    hexadecimal = ""

    while decimal > 0:
        resto = decimal % 16
        hexadecimal = hex_dig[resto] + hexadecimal
        decimal = decimal // 16
    
    return hexadecimal

num_decimal = int(input())

resultado = decimal_to_hex(num_decimal)

print(resultado)



