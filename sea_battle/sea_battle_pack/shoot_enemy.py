import mod_ships
import mod_board
import random

winner = ""
seq = [(4, 1), (3, 2), (2, 3), (1, 4), (8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8),
                  (10, 3), (9, 4), (8, 5), (7, 6), (6, 7), (5, 8), (4, 9), (3, 10), (10, 7), (9, 8), (8, 9), (7, 10),
                  (2, 1), (1, 2), (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (10, 1), (9, 2), (8, 3), (7, 4),
                  (6, 5), (5, 6), (4, 7), (3, 8), (2, 9), (1, 10), (10, 5), (9, 6), (8, 7), (7, 8), (6, 9), (5, 10),
                  (10, 9), (9, 10)]


def shoot_en(x):
    flag = True
    global winner
    global seq

    while flag:
        sum_1 = 0
        for i in range(1, 11):
            for j in range(1, 11):
                if x[i][j] == 3:
                    sum_1 += x[i][j]
        if sum_1 == 60:
            print("Ворог переміг! Наступного разу бий без жалю!!!")
            winner = "enemy"
            break

        # print(input("Постріл ворога. Натисніть клавішу Enter: "))
        n = -1
        while n < 49:
            flag = False
            n += 1
            if x[seq[n][0]][seq[n][1]] == 1:
                continue
            if x[seq[n][0]][seq[n][1]] == 3:
                continue
            elif x[seq[n][0]][seq[n][1]] == 0:
                x[seq[n][0]][seq[n][1]] = 1
                x.board_print()
                print(input("Ворог не поцілив. Натисніть клавішу Enter: "))
                break
            elif x[seq[n][0]][seq[n][1]] == 2:
                x[seq[n][0]][seq[n][1]] = 3
                x.board_print()
                print(input("Ворог поцілив. Натисніть клавішу Enter: "))
                for y in range(10):
                    if (seq[n][0], seq[n][1]) in mod_ships.pl_ships[y]:
                        for u in range(len(mod_ships.pl_ships[y])):
                            if x[mod_ships.pl_ships[y][u][0]][mod_ships.pl_ships[y][u][1]] != 3:
                                flag = True
                                break
                if flag:
                    for m in range(1, 4):
                        if x[seq[n][0] - n][seq[n][1]] == 1:
                            continue
                        if x[seq[n][0] - n][seq[n][1]] == 3:
                            continue
                        elif x[seq[n][0] - n][seq[n][1]] == 0:
                            x[seq[n][0] - n][seq[n][1]] = 1
                            x.board_print()
                            print(input("Ворог не поцілив. Натисніть клавішу Enter: "))
                            break
                        elif x[seq[n][0] - n][seq[n][1]] == 2:
                            x[seq[n][0] - n][seq[n][1]] = 3
                            x.board_print()
                            print(input("Ворог поцілив. Натисніть клавішу Enter: "))




                else:
                    for y in range(10):
                        if (seq[n][0], seq[n][1]) in mod_ships.pl_ships[y]:
                            if len(mod_ships.pl_ships[y]) == 1:
                                x[mod_ships.pl_ships[y][0][0] - 1][mod_ships.pl_ships[y][0][1] - 1] = 1
                                x[mod_ships.pl_ships[y][0][0] - 1][mod_ships.pl_ships[y][0][1]] = 1
                                x[mod_ships.pl_ships[y][0][0] - 1][mod_ships.pl_ships[y][0][1] + 1] = 1
                                x[mod_ships.pl_ships[y][0][0]][mod_ships.pl_ships[y][0][1] - 1] = 1
                                x[mod_ships.pl_ships[y][0][0]][mod_ships.pl_ships[y][0][1] + 1] = 1
                                x[mod_ships.pl_ships[y][0][0] + 1][mod_ships.pl_ships[y][0][1] - 1] = 1
                                x[mod_ships.pl_ships[y][0][0] + 1][mod_ships.pl_ships[y][0][1]] = 1
                                x[mod_ships.pl_ships[y][0][0] + 1][mod_ships.pl_ships[y][0][1] + 1] = 1
                                x.board_print()
                                flag = True
                                continue
                            else:
                                if mod_ships.pl_ships[y][0][0] == mod_ships.pl_ships[y][1][0]:
                                    x[mod_ships.pl_ships[y][0][0]][mod_ships.pl_ships[y][0][1] - 1] = 1
                                    x[mod_ships.pl_ships[y][len(mod_ships.pl_ships[y]) - 1][0]][
                                        mod_ships.pl_ships[y][len(mod_ships.pl_ships[y]) - 1][1] + 1] = 1
                                    for u in range(len(mod_ships.pl_ships[y]) + 2):
                                        x[mod_ships.pl_ships[y][0][0] - 1][
                                            mod_ships.pl_ships[y][0][1] - 1 + u] = 1
                                        x[mod_ships.pl_ships[y][0][0] + 1][
                                            mod_ships.pl_ships[y][0][1] - 1 + u] = 1
                                        x.board_print()
                                        flag = True
                                        continue
                                else:
                                    x[mod_ships.pl_ships[y][0][0] - 1][mod_ships.pl_ships[y][0][1]] = 1
                                    x[mod_ships.pl_ships[y][len(mod_ships.pl_ships[y]) - 1][0] + 1][
                                        mod_ships.pl_ships[y][len(mod_ships.pl_ships[y]) - 1][1]] = 1
                                    for u in range(len(mod_ships.pl_ships[y]) + 2):
                                        x[mod_ships.pl_ships[y][0][0] - 1 + u][
                                            mod_ships.pl_ships[y][0][1] - 1] = 1
                                        x[mod_ships.pl_ships[y][0][0] - 1 + u][
                                            mod_ships.pl_ships[y][0][1] + 1] = 1
                                        x.board_print()
                                        flag = True
                                        continue
















