num = int(input("Input number: "))

while num > 0:
    num_1 = num
    a = num % 10
    while num_1 > 0:
        c = num_1 // 10
        b = c % 10
        if a == b:
            print("Yes")
            break
        else:
            num_1 //= 10
    if a == b:
        break
    else:
        num //= 10
else:
    print("No")
