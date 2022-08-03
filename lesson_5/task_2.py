
N = int(input("Input number: "))
pull = range(1, N+1)
for i in pull:
    a = i * i
    b = 1
    c = i
    while c > 0:
        c //= 10
        b *= 10
    if i == a % b:
        print(i)
