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


def pos_rand_en(board):
    import random
    flag = False

    for i in range(1000):
        k = random.randint(0, 1)
        if k == 0:
            i = random.randint(0, 6)
            j = random.randint(20, 29)
            if i == 0:
                if j == 29:
                    for a in range(i, i + 5):
                        for b in range(j - 1, j + 1):
                            if board[a][b] != 0:
                                flag = True
                                break
                    if flag:
                        board[i][j] = board[i][j]
                        board[i + 1][j] = board[i + 1][j]
                        board[i + 2][j] = board[i + 2][j]
                        board[i + 3][j] = board[i + 3][j]
                    else:
                        board[i][j] = 3
                        board[i + 1][j] = 3
                        board[i + 2][j] = 3
                        board[i + 3][j] = 3
                        break
                else:
                    for a in range(i, i + 5):
                        for b in range(j - 1, j + 2):
                            if board[a][b] != 0:
                                flag = True
                                break
                    if flag:
                        board[i][j] = board[i][j]
                        board[i + 1][j] = board[i + 1][j]
                        board[i + 2][j] = board[i + 2][j]
                        board[i + 3][j] = board[i + 3][j]
                    else:
                        board[i][j] = 3
                        board[i + 1][j] = 3
                        board[i + 2][j] = 3
                        board[i + 3][j] = 3
                        break
            elif i == 6:
                if j == 29:
                    for a in range(i - 1, i + 4):
                        for b in range(j - 1, j + 1):
                            if board[a][b] != 0:
                                flag = True
                                break
                    if flag:
                        board[i][j] = board[i][j]
                        board[i + 1][j] = board[i + 1][j]
                        board[i + 2][j] = board[i + 2][j]
                        board[i + 3][j] = board[i + 3][j]
                    else:
                        board[i][j] = 3
                        board[i + 1][j] = 3
                        board[i + 2][j] = 3
                        board[i + 3][j] = 3
                        break
                else:
                    for a in range(i - 1, i + 4):
                        for b in range(j - 1, j + 2):
                            if board[a][b] != 0:
                                flag = True
                                break
                    if flag:
                        board[i][j] = board[i][j]
                        board[i + 1][j] = board[i + 1][j]
                        board[i + 2][j] = board[i + 2][j]
                        board[i + 3][j] = board[i + 3][j]
                    else:
                        board[i][j] = 3
                        board[i + 1][j] = 3
                        board[i + 2][j] = 3
                        board[i + 3][j] = 3
                        break
            else:
                if j == 29:
                    for a in range(i - 1, i + 5):
                        for b in range(j - 1, j + 1):
                            if board[a][b] != 0:
                                flag = True
                                break
                    if flag:
                        board[i][j] = board[i][j]
                        board[i + 1][j] = board[i + 1][j]
                        board[i + 2][j] = board[i + 2][j]
                        board[i + 3][j] = board[i + 3][j]
                    else:
                        board[i][j] = 3
                        board[i + 1][j] = 3
                        board[i + 2][j] = 3
                        board[i + 3][j] = 3
                        break
                else:
                    for a in range(i - 1, i + 5):
                        for b in range(j - 1, j + 2):
                            if board[a][b] != 0:
                                flag = True
                                break
                    if flag:
                        board[i][j] = board[i][j]
                        board[i + 1][j] = board[i + 1][j]
                        board[i + 2][j] = board[i + 2][j]
                        board[i + 3][j] = board[i + 3][j]
                    else:
                        board[i][j] = 3
                        board[i + 1][j] = 3
                        board[i + 2][j] = 3
                        board[i + 3][j] = 3
                        break
        # **********************************************************************************************************
        # **********************************************************************************************************
        # **********************************************************************************************************
        else:
            i = random.randint(0, 9)
            j = random.randint(20, 26)
            if i == 0:
                if j == 26:
                    for a in range(i, i + 2):
                        for b in range(j - 1, j + 4):
                            if board[a][b] != 0:
                                flag = True
                                break
                    if flag:
                        board[i][j] = board[i][j]
                        board[i][j + 1] = board[i][j + 1]
                        board[i][j + 2] = board[i][j + 2]
                        board[i][j + 3] = board[i][j + 3]
                    else:
                        board[i][j] = 3
                        board[i][j + 1] = 3
                        board[i][j + 2] = 3
                        board[i][j + 3] = 3
                        break
                else:
                    for a in range(i - 1, i + 2):
                        for b in range(j - 1, j + 5):
                            if board[a][b] != 0:
                                flag = True
                                break
                    if flag:
                        board[i][j] = board[i][j]
                        board[i][j + 1] = board[i][j + 1]
                        board[i][j + 2] = board[i][j + 2]
                        board[i][j + 3] = board[i][j + 3]
                    else:
                        board[i][j] = 3
                        board[i][j + 1] = 3
                        board[i][j + 2] = 3
                        board[i][j + 3] = 3
                        break
            elif i == 9:
                if j == 26:
                    for a in range(i - 1, i + 1):
                        for b in range(j - 1, j + 4):
                            if board[a][b] != 0:
                                flag = True
                                break
                    if flag:
                        board[i][j] = board[i][j]
                        board[i][j + 1] = board[i][j + 1]
                        board[i][j + 2] = board[i][j + 2]
                        board[i][j + 3] = board[i][j + 3]
                    else:
                        board[i][j] = 3
                        board[i][j + 1] = 3
                        board[i][j + 2] = 3
                        board[i][j + 3] = 3
                        break
                else:
                    for a in range(i - 1, i + 1):
                        for b in range(j - 1, j + 5):
                            if board[a][b] != 0:
                                flag = True
                                break
                    if flag:
                        board[i][j] = board[i][j]
                        board[i][j + 1] = board[i][j + 1]
                        board[i][j + 2] = board[i][j + 2]
                        board[i][j + 3] = board[i][j + 3]
                    else:
                        board[i][j] = 3
                        board[i][j + 1] = 3
                        board[i][j + 2] = 3
                        board[i][j + 3] = 3
                        break
            else:
                if j == 26:
                    for a in range(i - 1, i + 1):
                        for b in range(j - 1, j + 4):
                            if board[a][b] != 0:
                                flag = True
                                break
                    if flag:
                        board[i][j] = board[i][j]
                        board[i][j + 1] = board[i][j + 1]
                        board[i][j + 2] = board[i][j + 2]
                        board[i][j + 3] = board[i][j + 3]
                    else:
                        board[i][j] = 3
                        board[i][j + 1] = 3
                        board[i][j + 2] = 3
                        board[i][j + 3] = 3
                        break
                else:
                    for a in range(i - 1, i + 1):
                        for b in range(j - 1, j + 5):
                            if board[a][b] != 0:
                                flag = True
                                break
                    if flag:
                        board[i][j] = board[i][j]
                        board[i][j + 1] = board[i][j + 1]
                        board[i][j + 2] = board[i][j + 2]
                        board[i][j + 3] = board[i][j + 3]
                    else:
                        board[i][j] = 3
                        board[i][j + 1] = 3
                        board[i][j + 2] = 3
                        board[i][j + 3] = 3
                        break

    for i in range(10):
        print(board[i])


if __name__ == "__main__":
    board: list = [[0 for i in range(30)] for j in range(10)]
    pos_rand_en(board)



