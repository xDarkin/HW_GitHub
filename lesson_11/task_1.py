
def sum_check(*args):
    m = args[0]
    x = args[1]
    n = m

    for i in range(len(m)-1):
        count = 1
        for j in range(count, len(n)):
            if m[i] + n[j] == x:
                print(True, m[i], "+", n[j], "=", x)
                break
        count += 1
        if m[i] + n[j] == x:
            break
    else:
        print(False)


sum_check([1, 4, 5, 6, 8, 10, 24, 3], 6)
sum_check([1, 4, 5, 12, 24], 50)
