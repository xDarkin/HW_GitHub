import mod_ships

winner = ""
seq = [(4, 1), (3, 2), (2, 3), (1, 4), (8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8), (10, 3), (9, 4),
       (8, 5), (7, 6), (6, 7), (5, 8), (4, 9), (3, 10), (10, 7), (9, 8), (8, 9), (7, 10), (2, 1), (1, 2), (6, 1),
       (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (10, 1), (9, 2), (8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8), (2, 9),
       (1, 10), (10, 5), (9, 6), (8, 7), (7, 8), (6, 9), (5, 10), (10, 9), (9, 10)]

seq_1 = [(1, 1), (3, 1), (2, 2), (1, 3), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (7, 1), (6, 2), (5, 3), (4, 4),
         (3, 5), (2, 6), (1, 7), (9, 1), (8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8), (1, 9), (10, 2),
         (9, 3), (8, 4), (7, 5), (6, 6), (5, 7), (4, 8), (3, 9), (2, 10), (10, 4), (9, 5), (8, 6), (7, 7), (6, 8),
         (5, 9), (4, 10), (10, 6), (9, 7), (8, 8), (7, 9), (6, 10), (10, 8), (9, 9), (8, 10), (10, 10)]


def shoot_en(x):
    flag = True
    global winner
    global seq
    global seq_1

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

        n = -1
        while n < 49:
            flag = False
            n += 1
            if x[seq[n][0]][seq[n][1]] == 1:
                continue
            if x[seq[n][0]][seq[n][1]] == 3:
                for y in range(10):
                    if (seq[n][0], seq[n][1]) in mod_ships.pl_ships[y]:
                        for u in range(len(mod_ships.pl_ships[y])):
                            if x[mod_ships.pl_ships[y][u][0]][mod_ships.pl_ships[y][u][1]] != 3:
                                flag = True
                                break
                if flag:
                    for m in range(1, 4):
                        if x[seq[n][0] - m][seq[n][1]] == 1:
                            for o in range(1, 4):
                                if x[seq[n][0] + o][seq[n][1]] == 1:
                                    for q in range(1, 4):
                                        if x[seq[n][0]][seq[n][1] - q] == 1:
                                            for w in range(1, 4):
                                                if x[seq[n][0]][seq[n][1] + w] == 1:
                                                    break
                                                elif x[seq[n][0]][seq[n][1] + w] == 3:
                                                    continue
                                                elif x[seq[n][0]][seq[n][1] + w] == 0:
                                                    x[seq[n][0]][seq[n][1] + w] = 1
                                                    x.board_print()
                                                    print(input("Ворог не поцілив. Натисніть клавішу Enter: "))
                                                    return
                                                elif x[seq[n][0]][seq[n][1] + w] == 2:
                                                    x[seq[n][0]][seq[n][1] + w] = 3
                                                    x.board_print()
                                                    print(input("Ворог поцілив. Натисніть клавішу Enter: "))
                                                    for y in range(10):
                                                        if (seq[n][0], seq[n][1]) in mod_ships.pl_ships[y]:
                                                            for u in range(len(mod_ships.pl_ships[y])):
                                                                if x[mod_ships.pl_ships[y][u][0]][
                                                                    mod_ships.pl_ships[y][u][1]] \
                                                                        != 3:
                                                                    flag = True
                                                                    break
                                                                else:
                                                                    flag = False
                                                    if flag:
                                                        continue
                                                    else:
                                                        dots(x, n)
                                                        flag = True
                                                        break
                                                if flag:
                                                    break
                                            if flag:
                                                break

                                        elif x[seq[n][0]][seq[n][1] - q] == 3:
                                            continue
                                        elif x[seq[n][0]][seq[n][1] - q] == 0:
                                            x[seq[n][0]][seq[n][1] - q] = 1
                                            x.board_print()
                                            print(input("Ворог не поцілив. Натисніть клавішу Enter: "))
                                            return
                                        elif x[seq[n][0]][seq[n][1] - q] == 2:
                                            x[seq[n][0]][seq[n][1] - q] = 3
                                            x.board_print()
                                            print(input("Ворог поцілив. Натисніть клавішу Enter: "))
                                            for y in range(10):
                                                if (seq[n][0], seq[n][1]) in mod_ships.pl_ships[y]:
                                                    for u in range(len(mod_ships.pl_ships[y])):
                                                        if x[mod_ships.pl_ships[y][u][0]][mod_ships.pl_ships[y][u][1]] \
                                                                != 3:
                                                            flag = True
                                                            break
                                                        else:
                                                            flag = False
                                            if flag:
                                                continue
                                            else:
                                                dots(x, n)
                                                flag = True
                                                break
                                        if flag:
                                            break
                                    if flag:
                                        break

                                elif x[seq[n][0] + o][seq[n][1]] == 3:
                                    continue
                                elif x[seq[n][0] + o][seq[n][1]] == 0:
                                    x[seq[n][0] + o][seq[n][1]] = 1
                                    x.board_print()
                                    print(input("Ворог не поцілив. Натисніть клавішу Enter: "))
                                    return
                                elif x[seq[n][0] + o][seq[n][1]] == 2:
                                    x[seq[n][0] + o][seq[n][1]] = 3
                                    x.board_print()
                                    print(input("Ворог поцілив. Натисніть клавішу Enter: "))
                                    for y in range(10):
                                        if (seq[n][0], seq[n][1]) in mod_ships.pl_ships[y]:
                                            for u in range(len(mod_ships.pl_ships[y])):
                                                if x[mod_ships.pl_ships[y][u][0]][mod_ships.pl_ships[y][u][1]] != 3:
                                                    flag = True
                                                    break
                                                else:
                                                    flag = False
                                    if flag:
                                        continue
                                    else:
                                        dots(x, n)
                                        flag = True
                                        break
                                if flag:
                                    break
                            if flag:
                                break

                        elif x[seq[n][0] - m][seq[n][1]] == 3:
                            continue
                        elif x[seq[n][0] - m][seq[n][1]] == 0:
                            x[seq[n][0] - m][seq[n][1]] = 1
                            x.board_print()
                            print(input("Ворог не поцілив. Натисніть клавішу Enter: "))
                            return
                        elif x[seq[n][0] - m][seq[n][1]] == 2:
                            x[seq[n][0] - m][seq[n][1]] = 3
                            x.board_print()
                            print(input("Ворог поцілив. Натисніть клавішу Enter: "))
                            for y in range(10):
                                if (seq[n][0], seq[n][1]) in mod_ships.pl_ships[y]:
                                    for u in range(len(mod_ships.pl_ships[y])):
                                        if x[mod_ships.pl_ships[y][u][0]][mod_ships.pl_ships[y][u][1]] != 3:
                                            flag = True
                                            break
                                        else:
                                            flag = False
                            if flag:
                                continue
                            else:
                                dots(x, n)
                                flag = True
                                break
                        if flag:
                            break
                    if flag:
                        break

            elif x[seq[n][0]][seq[n][1]] == 0:
                x[seq[n][0]][seq[n][1]] = 1
                x.board_print()
                print(input("Ворог не поцілив. Натисніть клавішу Enter: "))
                flag = False
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
                        if x[seq[n][0] - m][seq[n][1]] == 1:
                            for o in range(1, 4):
                                if x[seq[n][0] + o][seq[n][1]] == 1:
                                    for q in range(1, 4):
                                        if x[seq[n][0]][seq[n][1] - q] == 1:
                                            for w in range(1, 4):
                                                if x[seq[n][0]][seq[n][1] + w] == 1:
                                                    break
                                                elif x[seq[n][0]][seq[n][1] + w] == 3:
                                                    continue
                                                elif x[seq[n][0]][seq[n][1] + w] == 0:
                                                    x[seq[n][0]][seq[n][1] + w] = 1
                                                    x.board_print()
                                                    print(input("Ворог не поцілив. Натисніть клавішу Enter: "))
                                                    return
                                                elif x[seq[n][0]][seq[n][1] + w] == 2:
                                                    x[seq[n][0]][seq[n][1] + w] = 3
                                                    x.board_print()
                                                    print(input("Ворог поцілив. Натисніть клавішу Enter: "))
                                                    for y in range(10):
                                                        if (seq[n][0], seq[n][1] + w) in mod_ships.pl_ships[y]:
                                                            for u in range(len(mod_ships.pl_ships[y])):
                                                                if x[mod_ships.pl_ships[y][u][0]][
                                                                    mod_ships.pl_ships[y][u][1]] \
                                                                        != 3:
                                                                    flag = True
                                                                    break
                                                                else:
                                                                    flag = False
                                                    if flag:
                                                        continue
                                                    else:
                                                        dots(x, n)
                                                        flag = True
                                                        break
                                                if flag:
                                                    break
                                            if flag:
                                                break

                                        elif x[seq[n][0]][seq[n][1] - q] == 3:
                                            continue
                                        elif x[seq[n][0]][seq[n][1] - q] == 0:
                                            x[seq[n][0]][seq[n][1] - q] = 1
                                            x.board_print()
                                            print(input("Ворог не поцілив. Натисніть клавішу Enter: "))
                                            return
                                        elif x[seq[n][0]][seq[n][1] - q] == 2:
                                            x[seq[n][0]][seq[n][1] - q] = 3
                                            x.board_print()
                                            print(input("Ворог поцілив. Натисніть клавішу Enter: "))
                                            for y in range(10):
                                                if (seq[n][0], seq[n][1] - q) in mod_ships.pl_ships[y]:
                                                    for u in range(len(mod_ships.pl_ships[y])):
                                                        if x[mod_ships.pl_ships[y][u][0]][mod_ships.pl_ships[y][u][1]] \
                                                                != 3:
                                                            flag = True
                                                            break
                                                        else:
                                                            flag = False
                                            if flag:
                                                continue
                                            else:
                                                dots(x, n)
                                                flag = True
                                                break
                                        if flag:
                                            break
                                    if flag:
                                        break

                                elif x[seq[n][0] + o][seq[n][1]] == 3:
                                    continue
                                elif x[seq[n][0] + o][seq[n][1]] == 0:
                                    x[seq[n][0] + o][seq[n][1]] = 1
                                    x.board_print()
                                    print(input("Ворог не поцілив. Натисніть клавішу Enter: "))
                                    return
                                elif x[seq[n][0] + o][seq[n][1]] == 2:
                                    x[seq[n][0] + o][seq[n][1]] = 3
                                    x.board_print()
                                    print(input("Ворог поцілив. Натисніть клавішу Enter: "))
                                    for y in range(10):
                                        if (seq[n][0] + o, seq[n][1]) in mod_ships.pl_ships[y]:
                                            for u in range(len(mod_ships.pl_ships[y])):
                                                if x[mod_ships.pl_ships[y][u][0]][mod_ships.pl_ships[y][u][1]] != 3:
                                                    flag = True
                                                    break
                                                else:
                                                    flag = False
                                    if flag:
                                        continue
                                    else:
                                        dots(x, n)
                                        flag = True
                                        break
                                if flag:
                                    break
                            if flag:
                                break

                        elif x[seq[n][0] - m][seq[n][1]] == 3:
                            continue
                        elif x[seq[n][0] - m][seq[n][1]] == 0:
                            x[seq[n][0] - m][seq[n][1]] = 1
                            x.board_print()
                            print(input("Ворог не поцілив. Натисніть клавішу Enter: "))
                            return
                        elif x[seq[n][0] - m][seq[n][1]] == 2:
                            x[seq[n][0] - m][seq[n][1]] = 3
                            x.board_print()
                            print(input("Ворог поцілив. Натисніть клавішу Enter: "))
                            for y in range(10):
                                if (seq[n][0] - m, seq[n][1]) in mod_ships.pl_ships[y]:
                                    for u in range(len(mod_ships.pl_ships[y])):
                                        if x[mod_ships.pl_ships[y][u][0]][mod_ships.pl_ships[y][u][1]] != 3:
                                            flag = True
                                            break
                                        else:
                                            flag = False
                            if flag:
                                continue
                            else:
                                dots(x, n)
                                flag = True
                                break
                        if flag:
                            break
                    if flag:
                        break

                else:
                    dots(x, n)
                    flag = True
                    break

        if n >= 49:
            a = -1
            while a < 49:
                flag = False
                a += 1
                if x[seq_1[a][0]][seq_1[a][1]] == 1 or x[seq_1[a][0]][seq_1[a][1]] == 3:
                    continue
                elif x[seq_1[a][0]][seq_1[a][1]] == 0:
                    x[seq_1[a][0]][seq_1[a][1]] = 1
                    x.board_print()
                    print(input("Ворог не поцілив. Натисніть клавішу Enter: "))
                    break
                elif x[seq_1[a][0]][seq_1[a][1]] == 2:
                    x[seq_1[a][0]][seq_1[a][1]] = 3
                    flag = True
                    x.board_print()
                    print(input("Ворог поцілив. Натисніть клавішу Enter: "))
                    if x[seq_1[a][0] - 1][seq_1[a][1]] == 0:
                        x[seq_1[a][0] - 1][seq_1[a][1]] = 1
                    if x[seq_1[a][0] + 1][seq_1[a][1]] == 0:
                        x[seq_1[a][0] + 1][seq_1[a][1]] = 1
                    for u in range(3):
                        if x[seq_1[a][0] - 1 + u][seq_1[a][1] - 1] == 0:
                            x[seq_1[a][0] - 1 + u][seq_1[a][1] - 1] = 1
                        if x[seq_1[a][0] - 1 + u][seq_1[a][1] + 1] == 0:
                            x[seq_1[a][0] - 1 + u][seq_1[a][1] + 1] = 1
                    x.board_print()
                    break


def dots(x, n):
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
