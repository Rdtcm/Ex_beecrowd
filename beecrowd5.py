def maior_num(a,b):
    maior_ab = int(((a+b+abs(a-b))/2))
    return maior_ab

a, b, c = [int(x) for x in input().split(" ")]

maior_ab = maior_num(a,b)
maior_abc = maior_num(maior_ab, c)

print(f"{maior_abc} eh o maior")