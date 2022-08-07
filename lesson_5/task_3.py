
sum_1 = 0
count = 0
count_1 = -1
count_2 = 0
min_1 = 0
max_1 = 0
while True:
    while True:
        i = int(input("Введіть ціле число: "))
        count += 1
        sum_1 += i
        if i > max_1 or max_1 == 0:
            max_1 = i
        if i < min_1 and i != 0 or min_1 == 0:
            min_1 = i
        if i % 2 == 0:
            count_1 += 1
        else:
            count_2 += 1
        if i == 0:
            break
    av = sum_1 / (count-1)
    print("Сума: ", sum_1)
    print("Середнє арифметичне: ", av)
    print("Максимальне число:", max_1, "; Мінімальне число:", min_1)
    print("Кількість парних:", count_1, "; Кількість непарних:", count_2)
    break
