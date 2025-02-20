import math as mt

def perimetro_triangulo(a,b,c):
    p = a + b + c
    return p

def area_trapezio(a,b,c):
    area = (1/2)*(c*(a+b))
    return area

a, b, c = [float(x) for x in input().split(" ")]

#verificando se é um triangulo
triangulo = False
if a > abs(b-c) and a < b+c:
    triangulo = True
elif b > abs(a-c) and b < a+c:
    triangulo = True
elif c > abs(a-b) and c < a+b:
    triangulo = True

if triangulo == True:
    perimetro = perimetro_triangulo(a,b,c)
    print(f"Perimetro = {perimetro}")
elif triangulo == False:
    area = area_trapezio(a,b,c)
    print(f"Area = {area}")