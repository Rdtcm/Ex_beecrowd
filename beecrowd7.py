n = int(input())
nums = []
cont = 0
cont2 = 0
for i in range(n):
    nums.append(int(input()))

for numero in nums:
    if numero >= 10 and numero <= 20:
        cont += 1
    else:
        cont2 += 1

print(f"{cont} in")
print(f"{cont2} out")
