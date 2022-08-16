
import random
n = [random.randint(1, 20) for i in range(0, 15)]
print(n)

sum_a = 0
sum_b = 0
for i in range(0, 15):
    if n[i] % 2 == 0:
        sum_b += n[i]
    else:
        sum_a += n[i]

if sum_a > sum_b:
    print("Yes")
else:
    print("No")
