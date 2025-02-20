condicao = True
alcool = 0
gasolina = 0 
diesel = 0

while condicao:
    num = int(input())
    if num == 4:
        condicao = False
    elif num == 1:
        alcool += 1
    elif num == 2:
        gasolina += 1
    elif num == 3:
        diesel += 1

print("MUITO OBRIGADO")
print(f"Alcool: {alcool}\nGasolina: {gasolina}\nDiesel: {diesel}")
