
import random
N = int(input("Input number: "))

a = [[random.randint(0, 20) for i in range(0, N)] for j in range(0, N)]

for i in range(0, N):
    print(a[i])

sum_d = 0
for i in range(0, N):
    sum_d += a[i][i]
print("Diagonal sum is:", sum_d)

sum_lc = 0
for i in range(0, N):
    sum_lc += a[i][N-1]
print("Last column sum is:", sum_lc)
