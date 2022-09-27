class BoardClass:
    board: list = [[0 for i in range(32)] for j in range(12)]
    for y in range(10):
        board[0][1 + y] = 1
        board[11][1 + y] = 1
        board[1 + y][0] = 1
        board[1 + y][11] = 1

    def board_print(self):
        a = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        print("                   ЗСУ                                           русня ")
        print(f"                потопив:{shoot_player.count_pl}                                      "
              f"потопив:{shoot_enemy.count_en}")
        print("┏━━━" + "┳━━━" * 9 + "┓" + " "*7 + "┏━━━" + "┳━━━" * 9 + "┓")
        for i in range(1, 11):
            for j in range(1, 11):
                print("┃", end="")
                if self[i][j] == 0:
                    print("", " ", end=" ")
                elif self[i][j] == 1:
                    print("", ".", end=" ")
                elif self[i][j] == 2:
                    print("", "▓", end=" ")
                else:
                    print("", "X", end=" ")
            print("┃  ", a[i-1], end="   ")
            for j in range(21, 31):
                print("┃", end="")
                if self[i][j] == 0:
                    print("", " ", end=" ")
                elif self[i][j] == 1:
                    print("", ".", end=" ")
                elif self[i][j] == 2:
                    print("", " ", end=" ")
                elif self[i][j] == 3:
                    print("", "X", end=" ")
            print("┃")
            print("┣━━━╋━━━╋━━━╋━━━╋━━━╋━━━╋━━━╋━━━╋━━━╋━━━┫" + " "*7 + "┣━━━╋━━━╋━━━╋━━━╋━━━╋━━━╋━━━╋━━━╋━━━╋━━━┫")
        print("┃ 1 ┃ 2 ┃ 3 ┃ 4 ┃ 5 ┃ 6 ┃ 7 ┃ 8 ┃ 9 ┃ 10┃" + " "*7 + "┃ 1 ┃ 2 ┃ 3 ┃ 4 ┃ 5 ┃ 6 ┃ 7 ┃ 8 ┃ 9 ┃ 10┃")
        print("┗━━━" + "┻━━━" * 9 + "┛" + " "*7 + "┗━━━" + "┻━━━" * 9 + "┛")

    def __getitem__(self, key):
        return self.board[key]

import shoot_enemy
import shoot_player

def count_pl(x):
    import mod_ships
    c_pl = 0
    for y in range(10):
        for u in range(len(mod_ships.en_ships[y])):
            if x[mod_ships.en_ships[y][u][0]][mod_ships.en_ships[y][u][1]] != 3:
                break
            c_pl += 1
    return c_pl


def count_en(x):
    import mod_ships
    c_en = 0
    for y in range(10):
        for u in range(len(mod_ships.pl_ships[y])):
            if x[mod_ships.pl_ships[y][u][0]][mod_ships.pl_ships[y][u][1]] != 3:
                break
            c_en += 1
    return c_en


if __name__ == "__main__":
    board = BoardClass()
    import mod_ships
    import shoot_player
    mod_ships.pos_rand_pl(board)
    ship = mod_ships.Ship()
    # shoot_player.shoot_pl(board)
    # mod_ships.pos_manual(board)
    mod_ships.pos_rand_en(board)
    board.board_print()
    print(board[0][0])


