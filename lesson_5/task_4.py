
N = int(input("Input number: "))
pull = range(1, N+1, 1)
for i in pull:
    if i**2 <= N:
        print(i**2)
