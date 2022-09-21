def pos_man(x, y):
    while True:
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

        while True:
            k_1 = input("Введіть положення корабля (0-вертикально, 1-горизонтально): ")
            if k_1.isdigit():
                if int(k_1) == 0:
                    k = 0
                    break
                elif int(k_1) == 1:
                    k = 1
                    break
                else:
                    print("Помилка вводу! Введіль 0 або 1!")
            else:
                print("Помилка вводу! Введіль 0 або 1!")

        flag = False
        if k == 0:
            if i == 0:
                if j == 9:
                    for a in range(i, i + y + 1):
                        for b in range(j - 1, j + 1):
                            if x[a][b] != 0:
                                flag = True
                                print("Неможливо розташувати! Між кораблями повинна бути вільна клітинка!")
                                break
                    if flag:
                        for n in range(y):
                            x[i + n][j] = x[i + n][j]
                    else:
                        for n in range(y):
                            x[i + n][j] = 2
                            break
                else:
                    for a in range(i, i + y + 1):
                        for b in range(j - 1, j + 2):
                            if x[a][b] != 0:
                                flag = True
                                print("Неможливо розташувати! Між кораблями повинна бути вільна клітинка!")
                                break
                    if flag:
                        for n in range(y):
                            x[i + n][j] = x[i + n][j]
                    else:
                        for n in range(y):
                            x[i + n][j] = 2
                            break
            elif i == 10 - y:
                if j == 9:
                    for a in range(i - 1, i + y):
                        for b in range(j - 1, j + 1):
                            if x[a][b] != 0:
                                flag = True
                                print("Неможливо розташувати! Між кораблями повинна бути вільна клітинка!")
                                break
                    if flag:
                        for n in range(y):
                            x[i + n][j] = x[i + n][j]
                    else:
                        for n in range(y):
                            x[i + n][j] = 2
                            break
                else:
                    for a in range(i - 1, i + y):
                        for b in range(j - 1, j + 2):
                            if x[a][b] != 0:
                                flag = True
                                print("Неможливо розташувати! Між кораблями повинна бути вільна клітинка!")
                                break
                    if flag:
                        for n in range(y):
                            x[i + n][j] = x[i + n][j]
                    else:
                        for n in range(y):
                            x[i + n][j] = 2
                            break
            else:
                if j == 9:
                    for a in range(i - 1, i + y + 1):
                        for b in range(j - 1, j + 1):
                            if x[a][b] != 0:
                                flag = True
                                print("Неможливо розташувати! Між кораблями повинна бути вільна клітинка!")
                                break
                    if flag:
                        for n in range(y):
                            x[i + n][j] = x[i + n][j]
                    else:
                        for n in range(y):
                            x[i + n][j] = 2
                            break
                else:
                    for a in range(i - 1, i + y + 1):
                        for b in range(j - 1, j + 2):
                            if x[a][b] != 0:
                                flag = True
                                print("Неможливо розташувати! Між кораблями повинна бути вільна клітинка!")
                                break
                    if flag:
                        for n in range(y):
                            x[i + n][j] = x[i + n][j]
                    else:
                        for n in range(y):
                            x[i + n][j] = 2
                            break
        # **********************************************************************************************************
        # **********************************************************************************************************
        # **********************************************************************************************************
        else:
            if i == 0:
                if j == 10 - y:
                    for a in range(i, i + 2):
                        for b in range(j - 1, j + y):
                            if x[a][b] != 0:
                                flag = True
                                print("Неможливо розташувати! Між кораблями повинна бути вільна клітинка!")
                                break
                    if flag:
                        for n in range(y):
                            x[i][j + n] = x[i][j + n]
                    else:
                        for n in range(y):
                            x[i][j + n] = 2
                            break
                else:
                    for a in range(i, i + 2):
                        for b in range(j - 1, j + y + 1):
                            if x[a][b] != 0:
                                flag = True
                                print("Неможливо розташувати! Між кораблями повинна бути вільна клітинка!")
                                break
                    if flag:
                        for n in range(y):
                            x[i][j + n] = x[i][j + n]
                    else:
                        for n in range(y):
                            x[i][j + n] = 2
                            break
            elif i == 9:
                if j == 10 - y:
                    for a in range(i - 1, i + 1):
                        for b in range(j - 1, j + y):
                            if x[a][b] != 0:
                                flag = True
                                print("Неможливо розташувати! Між кораблями повинна бути вільна клітинка!")
                                break
                    if flag:
                        for n in range(y):
                            x[i][j + n] = x[i][j + n]
                    else:
                        for n in range(y):
                            x[i][j + n] = 2
                            break
                else:
                    for a in range(i - 1, i + 1):
                        for b in range(j - 1, j + y + 1):
                            if x[a][b] != 0:
                                flag = True
                                print("Неможливо розташувати! Між кораблями повинна бути вільна клітинка!")
                                break
                    if flag:
                        for n in range(y):
                            x[i][j + n] = x[i][j + n]
                    else:
                        for n in range(y):
                            x[i][j + n] = 2
                            break
            else:
                if j == 10 - y:
                    for a in range(i - 1, i + 2):
                        for b in range(j - 1, j + y):
                            if x[a][b] != 0:
                                flag = True
                                print("Неможливо розташувати! Між кораблями повинна бути вільна клітинка!")
                                break
                    if flag:
                        for n in range(y):
                            x[i][j + n] = x[i][j + n]
                    else:
                        for n in range(y):
                            x[i][j + n] = 2
                            break
                else:
                    for a in range(i - 1, i + 2):
                        for b in range(j - 1, j + y + 1):
                            if x[a][b] != 0:
                                flag = True
                                print("Неможливо розташувати! Між кораблями повинна бути вільна клітинка!")
                                break
                    if flag:
                        for n in range(y):
                            x[i][j + n] = x[i][j + n]
                    else:
                        for n in range(y):
                            x[i][j + n] = 2
                            break
