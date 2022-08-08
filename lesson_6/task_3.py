
n = 0
v = "123456789"
num = input("Input number from 3 to 9: ")
if num.isnumeric() and int(num) >= 3 and int(num) <= 9:
    for i in range(0, int(num)):
        print(v[0:n:1] + v[n:-10:-1])                       # цифры слева
#        print((v[0:n:1] + v[n:-10:-1]).center(17))          # цифры по центру
#        print((v[0:n:1] + v[n:-10:-1]).rjust(17, " "))      # цифры справа
        n += 1
else:
    print("Wrong input!")
