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

    for t in range(10000):
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


if __name__ == "__main__":
    board: list = [[0 for i in range(30)] for j in range(10)]
    pos_rand_en(board)
    for i in range(10):
        print(board[i])
