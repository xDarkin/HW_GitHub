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


p = []
en_ships = []
pl_ships = []


def pos_rand(x, y):
    import random
    global p
    for t in range(1000):
        flag = False
        k = random.randint(0, 1)
        if k == 0:
            i = random.randint(1, 11 - y)
            j = random.randint(21, 30)
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
                v = [(i + n, j) for n in range(y)]
                p = v
                break
        # **********************************************************************************************************
        else:
            i = random.randint(1, 10)
            j = random.randint(21, 31 - y)
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
                v = [(i, j + n) for n in range(y)]
                p = v
                break


def pos_rand_en(x):
    ship = Ship()
    pos_rand(x, ship.ship_41)
    en_ship_41 = p
    pos_rand(x, ship.ship_31)
    en_ship_31 = p
    pos_rand(x, ship.ship_32)
    en_ship_32 = p
    pos_rand(x, ship.ship_21)
    en_ship_21 = p
    pos_rand(x, ship.ship_22)
    en_ship_22 = p
    pos_rand(x, ship.ship_23)
    en_ship_23 = p
    pos_rand(x, ship.ship_11)
    en_ship_11 = p
    pos_rand(x, ship.ship_12)
    en_ship_12 = p
    pos_rand(x, ship.ship_13)
    en_ship_13 = p
    pos_rand(x, ship.ship_14)
    en_ship_14 = p
    global en_ships
    en_ships = [en_ship_41, en_ship_31, en_ship_32, en_ship_21, en_ship_22, en_ship_23,
                en_ship_11, en_ship_12, en_ship_13, en_ship_14]


def pos_rand_1(x, y):
    import random
    global p
    for t in range(1000):
        flag = False
        k = random.randint(0, 1)
        if k == 0:
            i = random.randint(1, 11 - y)
            j = random.randint(1, 10)
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
                v = [(i + n, j) for n in range(y)]
                p = v
                break
        # **********************************************************************************************************
        else:
            i = random.randint(1, 10)
            j = random.randint(1, 11 - y)
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
                v = [(i, j + n) for n in range(y)]
                p = v
                break


def pos_rand_pl(x):
    ship = Ship()
    pos_rand_1(x, ship.ship_41)
    pl_ship_41 = p
    pos_rand_1(x, ship.ship_31)
    pl_ship_31 = p
    pos_rand_1(x, ship.ship_32)
    pl_ship_32 = p
    pos_rand_1(x, ship.ship_21)
    pl_ship_21 = p
    pos_rand_1(x, ship.ship_22)
    pl_ship_22 = p
    pos_rand_1(x, ship.ship_23)
    pl_ship_23 = p
    pos_rand_1(x, ship.ship_11)
    pl_ship_11 = p
    pos_rand_1(x, ship.ship_12)
    pl_ship_12 = p
    pos_rand_1(x, ship.ship_13)
    pl_ship_13 = p
    pos_rand_1(x, ship.ship_14)
    pl_ship_14 = p
    global pl_ships
    pl_ships = [pl_ship_41, pl_ship_31, pl_ship_32, pl_ship_21, pl_ship_22, pl_ship_23,
                pl_ship_11, pl_ship_12, pl_ship_13, pl_ship_14]


def pos_man(x, y):
    flag = True
    global p
    while flag:
        while True:
            i_1 = input("Введіть літеру першої клітинки (А, В, С, ...): ")
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
                    j = int(j_1)
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

        if k == 0 and i > 11 - y:
            print("Корабель виходить за межі поля!")
            flag = True
            continue

        if k == 1 and j > 11 - y:
            print("Корабель виходить за межі поля!")
            flag = True
            continue

        if k == 0:
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
                v = [(i + n, j) for n in range(y)]
                p = v
                break
        # **********************************************************************************************************
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
                v = [(i, j + n) for n in range(y)]
                p = v
                break


def pos_manual(x):
    import mod_board
    x = mod_board.BoardClass()
    ship = Ship()
    x.board_print()
    print("Розмістіть чотирипалубник:")
    pos_man(x, ship.ship_41)
    pl_ship_41 = p
    x.board_print()
    print("Розмістіть трипалубник:")
    pos_man(x, ship.ship_31)
    pl_ship_31 = p
    x.board_print()
    print("Розмістіть трипалубник:")
    pos_man(x, ship.ship_32)
    pl_ship_32 = p
    x.board_print()
    print("Розмістіть двопалубник:")
    pos_man(x, ship.ship_21)
    pl_ship_21 = p
    x.board_print()
    print("Розмістіть двопалубник:")
    pos_man(x, ship.ship_22)
    pl_ship_22 = p
    x.board_print()
    print("Розмістіть двопалубник:")
    pos_man(x, ship.ship_23)
    pl_ship_23 = p
    x.board_print()
    print("Розмістіть однопалубник:")
    pos_man(x, ship.ship_11)
    pl_ship_11 = p
    x.board_print()
    print("Розмістіть однопалубник:")
    pos_man(x, ship.ship_12)
    pl_ship_12 = p
    x.board_print()
    print("Розмістіть однопалубник:")
    pos_man(x, ship.ship_13)
    pl_ship_13 = p
    x.board_print()
    print("Розмістіть однопалубник:")
    pos_man(x, ship.ship_14)
    pl_ship_14 = p
    x.board_print()
    global pl_ships
    pl_ships = [pl_ship_41, pl_ship_31, pl_ship_32, pl_ship_21, pl_ship_22, pl_ship_23,
                pl_ship_11, pl_ship_12, pl_ship_13, pl_ship_14]


if __name__ == "__main__":
    board: list = [[0 for i in range(30)] for j in range(10)]
    pos_rand_en(board)
    pos_rand_pl(board)
    for i in range(10):
        print(board[i])
