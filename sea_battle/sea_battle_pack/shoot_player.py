import mod_ships


def shoot_pl(x):
    flag = True

    while flag:
        sum_1 = 0
        for i in range(1, 11):
            for j in range(21, 31):
                if x[i][j] == 3:
                    sum_1 += x[i][j]
        if sum_1 == 60:
            print("Вітаємо! Ви перемогли!!! Слава ЗСУ!!!")
            break

        while True:
            flag = False
            print("Ваш постріл! Оберіть клітинку: ")
            i_1 = input("Введіть літеру клітинки (А, В, С, ...): ")
            if i_1 == "A" or i_1 == "a":
                i = 1
                break
            elif i_1 == "B" or i_1 == "b":
                i = 2
                break
            elif i_1 == "C" or i_1 == "c":
                i = 3
                break
            elif i_1 == "D" or i_1 == "d":
                i = 4
                break
            elif i_1 == "E" or i_1 == "e":
                i = 5
                break
            elif i_1 == "F" or i_1 == "f":
                i = 6
                break
            elif i_1 == "G" or i_1 == "g":
                i = 7
                break
            elif i_1 == "H" or i_1 == "h":
                i = 8
                break
            elif i_1 == "I" or i_1 == "i":
                i = 9
                break
            elif i_1 == "J" or i_1 == "j":
                i = 10
                break
            else:
                print("Помилка вводу! Введіль літеру від A до J!")

        while True:
            j_1 = input("Введіть номер стовпця (від 1 до 10): ")
            if j_1.isdigit():
                if 1 <= int(j_1) <= 10:
                    j = int(j_1) + 20
                    break
                else:
                    print("Помилка вводу! Введіль цифру від 1 до 10!")
            else:
                print("Помилка вводу! Введіль цифру від 1 до 10!")

        if x[i][j] == 1 or x[i][j] == 3:
            print("В цю клітинку вже було влучання! Оберіть іншу!")
            flag = True
            continue

        if x[i][j] == 0:
            x[i][j] = 1
            print("\n"*50)
            x.board_print()
            print("Ви не поцілили!")
            break

        if x[i][j] == 2:
            x[i][j] = 3
            for y in range(10):
                if (i, j) in mod_ships.en_ships[y]:
                    for u in range(len(mod_ships.en_ships[y])):
                        if x[mod_ships.en_ships[y][u][0]][mod_ships.en_ships[y][u][1]] != 3:
                            flag = True
                            print("\n" * 50)
                            x.board_print()
                            print("Є влучення!")
                            break
            if flag:
                continue
            else:
                for y in range(10):
                    if (i, j) in mod_ships.en_ships[y]:
                        if len(mod_ships.en_ships[y]) == 1:
                            x[mod_ships.en_ships[y][0][0] - 1][mod_ships.en_ships[y][0][1] - 1] = 1
                            x[mod_ships.en_ships[y][0][0] - 1][mod_ships.en_ships[y][0][1]] = 1
                            x[mod_ships.en_ships[y][0][0] - 1][mod_ships.en_ships[y][0][1] + 1] = 1
                            x[mod_ships.en_ships[y][0][0]][mod_ships.en_ships[y][0][1] - 1] = 1
                            x[mod_ships.en_ships[y][0][0]][mod_ships.en_ships[y][0][1] + 1] = 1
                            x[mod_ships.en_ships[y][0][0] + 1][mod_ships.en_ships[y][0][1] - 1] = 1
                            x[mod_ships.en_ships[y][0][0] + 1][mod_ships.en_ships[y][0][1]] = 1
                            x[mod_ships.en_ships[y][0][0] + 1][mod_ships.en_ships[y][0][1] + 1] = 1
                            print("\n" * 50)
                            x.board_print()
                            print("Є влучення!")
                            flag = True
                            continue
                        else:
                            if mod_ships.en_ships[y][0][0] == mod_ships.en_ships[y][1][0]:
                                x[mod_ships.en_ships[y][0][0]][mod_ships.en_ships[y][0][1] - 1] = 1
                                x[mod_ships.en_ships[y][len(mod_ships.en_ships[y]) - 1][0]][
                                    mod_ships.en_ships[y][len(mod_ships.en_ships[y]) - 1][1] + 1] = 1
                                for u in range(len(mod_ships.en_ships[y]) + 2):
                                    x[mod_ships.en_ships[y][0][0] - 1][mod_ships.en_ships[y][0][1] - 1 + u] = 1
                                    x[mod_ships.en_ships[y][0][0] + 1][mod_ships.en_ships[y][0][1] - 1 + u] = 1
                                    print("\n" * 50)
                                    x.board_print()
                                    print("Є влучення!")
                                    flag = True
                                    continue
                            else:
                                x[mod_ships.en_ships[y][0][0] - 1][mod_ships.en_ships[y][0][1]] = 1
                                x[mod_ships.en_ships[y][len(mod_ships.en_ships[y]) - 1][0] + 1][
                                    mod_ships.en_ships[y][len(mod_ships.en_ships[y]) - 1][1]] = 1
                                for u in range(len(mod_ships.en_ships[y]) + 2):
                                    x[mod_ships.en_ships[y][0][0] - 1 + u][mod_ships.en_ships[y][0][1] - 1] = 1
                                    x[mod_ships.en_ships[y][0][0] - 1 + u][mod_ships.en_ships[y][0][1] + 1] = 1
                                    print("\n" * 50)
                                    x.board_print()
                                    print("Є влучення!")
                                    flag = True
                                    continue
