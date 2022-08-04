
sum1 = 0
count = 0
count_1 = -1
count_2 = 0
while True:
    while True:
        i = int(input("Введіть ціле число: "))
        count += 1
        sum1 += i
        if (sum1 / count) <= ((i + i) / 2):
            max1 = i
        else:
            max1 = max1
        if (sum1 / count) >= ((i + i) / 2):
            min1 = i
        else:
            min1 = min1
        if i % 2 == 0:
            count_1 += 1
        else:
            count_2 += 1
        if i == 0:
            break
    av = sum1 / (count-1)
    print("Сума: ", sum1)
    print("Середнє арифметичне: ", av)
    print("Максимальне число:", max1, "; Мінімальне число:", min1)
    print("Кількість парних:", count_1, "; Кількість непарних:", count_2)
    break
