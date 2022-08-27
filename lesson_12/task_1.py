
import random
while True:
    m = int(input("Введіть ціле число більше 5: "))
    if m <= 5:
        print("Помилка! Введіть ціле число більше 5: ")
    else:
        break
a = [[random.randint(1, 50) for i in range(m)] for j in range(m)]
b = [sum([a[i][j] for i in range(m)]) for j in range(m)]


def printing(func):
    def wrap():
        print("До сортування:")
        for i in range(m):
            print("")
            for j in range(m):
                print(str(a[i][j]).ljust(4, " "), end=" ")
        print("")
        for i in range(m):
            print(str(b[i]).ljust(4, " "), end=" ")
        print("\n")
        func()
        print("Після сортування:")
        for i in range(m):
            print("")
            for j in range(m):
                print(str(a[i][j]).ljust(4, " "), end=" ")
        print("")
        for i in range(m):
            print(str(b[i]).ljust(4, " "), end=" ")
        print("\n")
    return wrap


@printing
def sort():
    for i in range(m - 1):
        for j in range(m - 2, i - 1, -1):
            if b[j + 1] < b[j]:
                b[j], b[j + 1] = b[j + 1], b[j]
                for k in range(m):
                    a[k][j], a[k][j + 1] = a[k][j + 1], a[k][j]

    for o in range(m):
        if o % 2 == 0:
            for i in range(m - 1):
                for j in range(m - 2, i - 1, -1):
                    if a[j + 1][o] > a[j][o]:
                        a[j][o], a[j + 1][o] = a[j + 1][o], a[j][o]
        else:
            for i in range(m - 1):
                for j in range(m - 2, i - 1, -1):
                    if a[j + 1][o] < a[j][o]:
                        a[j][o], a[j + 1][o] = a[j + 1][o], a[j][o]

    return a, b


sort()
