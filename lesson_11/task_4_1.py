k = {}


def table(func):

    def wrapper():
        func()
        global k
        k = list(k)
        k.sort()
        print(" ", "_"*len(str(k[-1])), " ", "_"*11, " ", "_"*8)
        for i in range(len(k)):
            print("|", str(k[i]).ljust(len(str(k[-1])), " "), "|", "кратне 3".ljust(11, " ") if k[i] % 3 == 0
                  else "не кратне 3".ljust(11, " "),
                  "|", "парне".ljust(8, " ") if k[i] % 2 == 0 else "не парне".ljust(8, " "), "|")
            print("|", "_" * len(str(k[-1])), "|", "_" * 11, "|", "_" * 8, "|")
    return wrapper


@table
def numbers():
    import random
    x = int(input("Input number: "))
    n = set(random.randint(1, 99999) for i in range(x))
    global k
    k = n


numbers()
