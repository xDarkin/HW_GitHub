while True:
    i_1 = input("Введіть літеру клітинки (А, В, С, ...): ")
    if i_1 == "A" or i_1 == "a":
        i = 0
        break
    elif i_1 == "B" or i_1 == "b":
        i = 1
        break
    elif i_1 == "C" or i_1 == "c":
        i = 2
        break
    elif i_1 == "D" or i_1 == "d":
        i = 3
        break
    elif i_1 == "E" or i_1 == "e":
        i = 4
        break
    elif i_1 == "F" or i_1 == "f":
        i = 5
        break
    elif i_1 == "G" or i_1 == "g":
        i = 6
        break
    elif i_1 == "H" or i_1 == "h":
        i = 7
        break
    elif i_1 == "I" or i_1 == "i":
        i = 8
        break
    elif i_1 == "J" or i_1 == "j":
        i = 9
        break
    else:
        print("Помилка вводу! Введіль літеру від A до J!")

while True:
    j_1 = input("Введіть номер стовпця (від 1 до 10): ")
    if j_1.isdigit():
        if 1 <= int(j_1) <= 10:
            j = int(j_1) - 1
            break
        else:
            print("Помилка вводу! Введіль цифру від 1 до 10!")
    else:
        print("Помилка вводу! Введіль цифру від 1 до 10!")