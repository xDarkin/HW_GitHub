
import random
m = list(range(1, 21))
dic = dict.fromkeys(m, 0)
for i in dic:
    dic[i] = random.randint(1, 20)
print(dic)

n = list(dic.values())
print(n)
v = 1
for i in n:
    v *= i
print(v)
