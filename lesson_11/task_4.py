
def table(func):

    def wrapper(*args, **kwargs):
        g = func(*args, **kwargs)
        g = list(g)
        g.sort()
        print(" ", "_"*len(str(g[-1])), " ", "_"*11, " ", "_"*8)
        for i in range(len(g)):
            print("|", str(g[i]).ljust(len(str(g[-1])), " "), "|", "кратне 3".ljust(11, " ") if g[i] % 3 == 0
                  else "не кратне 3".ljust(11, " "),
                  "|", "парне".ljust(8, " ") if g[i] % 2 == 0 else "не парне".ljust(8, " "), "|")
            print("|", "_" * len(str(g[-1])), "|", "_" * 11, "|", "_" * 8, "|")
    return wrapper


@table
def numbers(x):
    import random
    n = set(random.randint(1, 99999) for i in range(x))
    return n


numbers(10)
