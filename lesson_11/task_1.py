
def sum_check():
    m = input("Введіть список чисел через пробіл: ")
    m = [int(i) for i in m.split()]
    x = int(input("Введіть число: "))
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


sum_check()
sum_check()
