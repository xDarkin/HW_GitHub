
import random
n = int(input("Введіть кількість рядків: "))
m = int(input("Введіть кількість ствопців: "))
a = [[random.randint(1, 50) for i in range(m)] for j in range(n)]
o = [sum([a[i][j] for i in range(n)]) for j in range(m)]


def sum_v(j):
    b = 0
    for i in range(m):
        b += a[j][i]
    return b


for i in range(n):
    for j in range(m):
        print(f"{a[i][j]:>3}", end=" ")
    print(f"{sum_v(i):>6}")
print("")
for i in range(m):
    print(f"{o[i]:>3}", end=" ")
print("")
