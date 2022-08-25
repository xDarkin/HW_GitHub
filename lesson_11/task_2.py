
m = list(map(lambda x, y=3: x**y, [1, 2, 3]))
n = list(map(lambda x, y=3: x**y, [3, 4, 5], [2, 3, 4]))
print(m)
print(n)
