
def gen(x, y):
    for i in range(x, y+1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                yield i


for n in gen(1, 100):
    print(n, end=" ")
