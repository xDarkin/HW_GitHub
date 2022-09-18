class BoardClass:
    board: list = [[0 for i in range(30)] for j in range(10)]

    def board_print(self):
        a = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        print("┏━━━" + "┳━━━" * 9 + "┓" + " "*7 + "┏━━━" + "┳━━━" * 9 + "┓")
        for i in range(10):
            for j in range(10):
                print("┃", end="")
                if self.board[i][j] == 0:
                    print("", " ", end=" ")
                elif self.board[i][j] == 1:
                    print("", ".", end=" ")
                elif self.board[i][j] == 2:
                    print("", "▓", end=" ")
                else:
                    print("", "X", end=" ")
            print("┃  ", a[i], end="   ")
            for j in range(20, 30):
                print("┃", end="")
                if board[i][j] == 0:
                    print("", " ", end=" ")
                elif board[i][j] == 1:
                    print("", ".", end=" ")
                else:
                    print("", "X", end=" ")
            print("┃")
            print("┣━━━╋━━━╋━━━╋━━━╋━━━╋━━━╋━━━╋━━━╋━━━╋━━━┫" + " "*7 + "┣━━━╋━━━╋━━━╋━━━╋━━━╋━━━╋━━━╋━━━╋━━━╋━━━┫")
        print("┃ 1 ┃ 2 ┃ 3 ┃ 4 ┃ 5 ┃ 6 ┃ 7 ┃ 8 ┃ 9 ┃ 10┃" + " "*7 + "┃ 1 ┃ 2 ┃ 3 ┃ 4 ┃ 5 ┃ 6 ┃ 7 ┃ 8 ┃ 9 ┃ 10┃")
        print("┗━━━" + "┻━━━" * 9 + "┛" + " "*7 + "┗━━━" + "┻━━━" * 9 + "┛")

    def __getitem__(self, key):
        return self.board[key]


if __name__ == "__main__":
    board = BoardClass()
    board[0][0] = 1
    board[1][1] = 2
    board[2][2] = 3
    board[0][20] = 3
    board[9][29] = 3
    board.board_print()
