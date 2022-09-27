import mod_ships
import mod_board
import shoot_player
import shoot_enemy

board = mod_board.BoardClass()
ship = mod_ships.Ship()

print("Вітаю у грі Sea Battle!!!")
g = input("Бажаєте розташувати Ваші кораблі самостійно? (Y-так, N-ні): ")
if g == "Y" or g == "y":
    mod_ships.pos_manual(board)
else:
    mod_ships.pos_rand_pl(board)
mod_ships.pos_rand_en(board)
board.board_print()
print("\n"*50)
print("Перший постріл за Вами!")
board.board_print()

while True:
    shoot_player.shoot_pl(board)
    sum_1 = 0
    for i in range(1, 11):
        for j in range(21, 31):
            if board[i][j] == 3:
                sum_1 += board[i][j]
    if sum_1 == 60:
        break

    shoot_enemy.shoot_en(board)
    sum_2 = 0
    for i in range(1, 11):
        for j in range(1, 11):
            if board[i][j] == 3:
                sum_2 += board[i][j]
    if sum_2 == 60:
        break
