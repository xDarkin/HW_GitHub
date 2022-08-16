
import random
n = [random.randint(1, 20) for i in range(0, 15)]
print(n)

sum_a = (n[i] if n[i] % 2 != 0 else 0 for i in range(0, 15))
sum_b = (n[i] if n[i] % 2 == 0 else 0 for i in range(0, 15))

print(sum(sum_a), sum(sum_b))
sum_a = (n[i] if n[i] % 2 != 0 else 0 for i in range(0, 15))
sum_b = (n[i] if n[i] % 2 == 0 else 0 for i in range(0, 15))

if sum(sum_a) > sum(sum_b):
    print("Yes")
else:
    print("No")
