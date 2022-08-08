
while True:
    line = input("Input two words divided by space: ")
    list_1 = list(line.split())
    if len(list_1) == 2 and list_1[0].isalpha() and list_1[1].isalpha():
        a = list_1[0]
        b = list_1[1]
        a = a[::-1]
        b = b[::-1]
        a = a.capitalize()
        b = b.capitalize()
        print(a, b)
        break
    else:
        print("Please input two words divided by space")
