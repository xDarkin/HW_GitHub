import mod_ships
import mod_board


def shoot_pl(x):
    flag = True
    while flag:
        while True:
            flag = False

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
                    j = int(j_1) - 1 + 20
                    break
                else:
                    print("Помилка вводу! Введіль цифру від 1 до 10!")
            else:
                print("Помилка вводу! Введіль цифру від 1 до 10!")

        if x[i][j] == 1 or x[i][j] == 3:
            print("В цю клітинку вже було влучання! Оберіть іншу!")
            flag = True
            break

        if x[i][j] == 0:
            x[i][j] = 1
            x.board_print()
            break

        if x[i][j] == 2:
            x[i][j] = 3
            for y in range(10):
                if (i, j) in mod_ships.en_ships[y]:
                    for u in range(len(mod_ships.en_ships[y])):
                        if x[mod_ships.en_ships[y][u][0]][mod_ships.en_ships[y][u][1]] != 3:
                            flag = True
                            x.board_print()
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
                            x.board_print()
                            continue
                        else:
                            if mod_ships.en_ships[y][0][0] == mod_ships.en_ships[y][1][0]:
                                x[mod_ships.en_ships[y][0][0]][mod_ships.en_ships[y][0][1] - 1] = 1
                                x[mod_ships.en_ships[y][len(mod_ships.en_ships[y]) - 1][0]][
                                    mod_ships.en_ships[y][len(mod_ships.en_ships[y]) - 1][1] + 1] = 1
                                for u in range(len(mod_ships.en_ships[y]) + 2):
                                    x[mod_ships.en_ships[y][0][0] - 1][mod_ships.en_ships[y][0][1] - 1 + u] = 1
                                    x[mod_ships.en_ships[y][0][0] + 1][mod_ships.en_ships[y][0][1] - 1 + u] = 1
                                    x.board_print()
                                    continue
                            else:
                                x[mod_ships.en_ships[y][0][0] - 1][mod_ships.en_ships[y][0][1]] = 1
                                x[mod_ships.en_ships[y][len(mod_ships.en_ships[y]) - 1][0] + 1][
                                    mod_ships.en_ships[y][len(mod_ships.en_ships[y]) - 1][1]] = 1
                                for u in range(len(mod_ships.en_ships[y]) + 2):
                                    x[mod_ships.en_ships[y][0][0] - 1 + u][mod_ships.en_ships[y][0][1] - 1] = 1
                                    x[mod_ships.en_ships[y][0][0] - 1 + u][mod_ships.en_ships[y][0][1] + 1] = 1
                                    x.board_print()
                                    continue

