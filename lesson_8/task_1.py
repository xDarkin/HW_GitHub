
N = int(input("Input number: "))

a = [[j if j % 2 == 0 else i - (N + 1) for i in range(1, N+1)] for j in range(1, N+1)]

for i in range(0, N):
    print(a[i])
