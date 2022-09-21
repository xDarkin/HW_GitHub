class Ship:
    ship_41 = 4
    ship_31 = 3
    ship_32 = 3
    ship_21 = 2
    ship_22 = 2
    ship_23 = 2
    ship_11 = 1
    ship_12 = 1
    ship_13 = 1
    ship_14 = 1


def pos_rand(x, y):
    import random

    for t in range(1000):
        flag = False
        k = random.randint(0, 1)
        if k == 0:
            i = random.randint(0, 10 - y)
            j = random.randint(20, 29)
            if i == 0:
                if j == 29:
                    for a in range(i, i + y + 1):
                        for b in range(j - 1, j + 1):
                            if x[a][b] != 0:
                                flag = True
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
                                break
                    if flag:
                        for n in range(y):
                            x[i + n][j] = x[i + n][j]
                    else:
                        for n in range(y):
                            x[i + n][j] = 2
                        break
            elif i == 10 - y:
                if j == 29:
                    for a in range(i - 1, i + y):
                        for b in range(j - 1, j + 1):
                            if x[a][b] != 0:
                                flag = True
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
                                break
                    if flag:
                        for n in range(y):
                            x[i + n][j] = x[i + n][j]
                    else:
                        for n in range(y):
                            x[i + n][j] = 2
                        break
            else:
                if j == 29:
                    for a in range(i - 1, i + y + 1):
                        for b in range(j - 1, j + 1):
                            if x[a][b] != 0:
                                flag = True
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
            i = random.randint(0, 9)
            j = random.randint(20, 30 - y)
            if i == 0:
                if j == 30 - y:
                    for a in range(i, i + 2):
                        for b in range(j - 1, j + y):
                            if x[a][b] != 0:
                                flag = True
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
                                break
                    if flag:
                        for n in range(y):
                            x[i][j + n] = x[i][j + n]
                    else:
                        for n in range(y):
                            x[i][j + n] = 2
                        break
            elif i == 9:
                if j == 30 - y:
                    for a in range(i - 1, i + 1):
                        for b in range(j - 1, j + y):
                            if x[a][b] != 0:
                                flag = True
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
                                break
                    if flag:
                        for n in range(y):
                            x[i][j + n] = x[i][j + n]
                    else:
                        for n in range(y):
                            x[i][j + n] = 2
                        break
            else:
                if j == 30 - y:
                    for a in range(i - 1, i + 2):
                        for b in range(j - 1, j + y):
                            if x[a][b] != 0:
                                flag = True
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
                                break
                    if flag:
                        for n in range(y):
                            x[i][j + n] = x[i][j + n]
                    else:
                        for n in range(y):
                            x[i][j + n] = 2
                        break


def pos_rand_en(x):
    ship = Ship()
    pos_rand(x, ship.ship_41)
    pos_rand(x, ship.ship_31)
    pos_rand(x, ship.ship_32)
    pos_rand(x, ship.ship_21)
    pos_rand(x, ship.ship_22)
    pos_rand(x, ship.ship_23)
    pos_rand(x, ship.ship_11)
    pos_rand(x, ship.ship_12)
    pos_rand(x, ship.ship_13)
    pos_rand(x, ship.ship_14)


def pos_rand_1(x, y):
    import random

    for t in range(1000):
        flag = False
        k = random.randint(0, 1)
        if k == 0:
            i = random.randint(0, 10 - y)
            j = random.randint(0, 9)
            if i == 0:
                if j == 9:
                    for a in range(i, i + y + 1):
                        for b in range(j - 1, j + 1):
                            if x[a][b] != 0:
                                flag = True
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
            i = random.randint(0, 9)
            j = random.randint(0, 10 - y)
            if i == 0:
                if j == 10 - y:
                    for a in range(i, i + 2):
                        for b in range(j - 1, j + y):
                            if x[a][b] != 0:
                                flag = True
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
                                break
                    if flag:
                        for n in range(y):
                            x[i][j + n] = x[i][j + n]
                    else:
                        for n in range(y):
                            x[i][j + n] = 2
                        break


def pos_rand_pl(x):
    ship = Ship()
    pos_rand_1(x, ship.ship_41)
    pos_rand_1(x, ship.ship_31)
    pos_rand_1(x, ship.ship_32)
    pos_rand_1(x, ship.ship_21)
    pos_rand_1(x, ship.ship_22)
    pos_rand_1(x, ship.ship_23)
    pos_rand_1(x, ship.ship_11)
    pos_rand_1(x, ship.ship_12)
    pos_rand_1(x, ship.ship_13)
    pos_rand_1(x, ship.ship_14)


def pos_man(x, y):
    flag = True
    while flag:
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

        if y > 1:
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
        else:
            k = 0

        flag = False

        if k == 0 and i > 10 - y:
            print("Корабель виходить за межі поля!")
            flag = True
            continue

        if k == 1 and j > 10 - y:
            print("Корабель виходить за межі поля!")
            flag = True
            continue

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


def pos_manual(x):
    ship = Ship()
    import mod_board
    x = mod_board.BoardClass()
    x.board_print()
    pos_man(x, ship.ship_41)
    x.board_print()
    pos_man(x, ship.ship_31)
    x.board_print()
    pos_man(x, ship.ship_32)
    x.board_print()
    pos_man(x, ship.ship_21)
    x.board_print()
    pos_man(x, ship.ship_22)
    x.board_print()
    pos_man(x, ship.ship_23)
    x.board_print()
    pos_man(x, ship.ship_11)
    x.board_print()
    pos_man(x, ship.ship_12)
    x.board_print()
    pos_man(x, ship.ship_13)
    x.board_print()
    pos_man(x, ship.ship_14)
    x.board_print()


if __name__ == "__main__":
    board: list = [[0 for i in range(30)] for j in range(10)]
    pos_rand_en(board)
    pos_rand_pl(board)
    for i in range(10):
        print(board[i])
