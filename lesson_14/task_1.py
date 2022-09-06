
def fn_1():
    m = input("Введіть перше значення: ")
    n = input("Введіть друге значення: ")
    try:
        m = int(m)
        n = int(n)
    except ValueError:
        a = str(m) + str(n)
    else:
        a = m + n
    print(a)


if __name__ == "__main__":
    fn_1()
