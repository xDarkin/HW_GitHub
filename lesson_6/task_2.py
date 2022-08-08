
a = input("Input a string: ")
b = input("Input a character: ")
for i in range(len(a)):
    if a[i] == b:
        print("Character", b, "occurred in index:", i)
