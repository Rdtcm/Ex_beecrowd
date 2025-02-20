horario = input()

if horario < '12':
    print("bom dia")
if horario > '12' and horario < '17':
    print("Boa tarde")
else:
    print("boa noite")