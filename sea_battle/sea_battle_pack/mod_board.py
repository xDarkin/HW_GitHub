class BoardClass:
    board: list = [[0 for i in range(30)] for j in range(10)]

    def board_print(self):
        a = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        print("                  ЗСУ                                          свинособаки ")
        print("┏━━━" + "┳━━━" * 9 + "┓" + " "*7 + "┏━━━" + "┳━━━" * 9 + "┓")
        for i in range(10):
            for j in range(10):
                print("┃", end="")
                if self[i][j] == 0:
                    print("", " ", end=" ")
                elif self[i][j] == 1:
                    print("", ".", end=" ")
                elif self[i][j] == 2:
                    print("", "▓", end=" ")
                else:
                    print("", "X", end=" ")
            print("┃  ", a[i], end="   ")
            for j in range(20, 30):
                print("┃", end="")
                if self[i][j] == 0:
                    print("", " ", end=" ")
                elif self[i][j] == 1:
                    print("", ".", end=" ")
                elif self[i][j] == 2:
                    print("", "▓", end=" ")
                elif self[i][j] == 3:
                    print("", "X", end=" ")
            print("┃")
            print("┣━━━╋━━━╋━━━╋━━━╋━━━╋━━━╋━━━╋━━━╋━━━╋━━━┫" + " "*7 + "┣━━━╋━━━╋━━━╋━━━╋━━━╋━━━╋━━━╋━━━╋━━━╋━━━┫")
        print("┃ 1 ┃ 2 ┃ 3 ┃ 4 ┃ 5 ┃ 6 ┃ 7 ┃ 8 ┃ 9 ┃ 10┃" + " "*7 + "┃ 1 ┃ 2 ┃ 3 ┃ 4 ┃ 5 ┃ 6 ┃ 7 ┃ 8 ┃ 9 ┃ 10┃")
        print("┗━━━" + "┻━━━" * 9 + "┛" + " "*7 + "┗━━━" + "┻━━━" * 9 + "┛")

    def __getitem__(self, key):
        return self.board[key]


if __name__ == "__main__":
    board = BoardClass()
    import mod_ships
    # mod_ships.pos_rand_en(board)
    # mod_ships.pos_rand_pl(board)
    ship = mod_ships.Ship()
    mod_ships.pos_manual(board)
    # board.board_print()

