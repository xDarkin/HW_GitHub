import mod_ships
import mod_board
import shoot_player

board = mod_board.BoardClass()
ship = mod_ships.Ship()

mod_ships.pos_rand_en(board)
board.board_print()
# mod_ships.pos_manual(board)
shoot_player.shoot_pl(board)
print("************************************************************")
shoot_player.shoot_pl(board)
print("************************************************************")
shoot_player.shoot_pl(board)
print("************************************************************")
shoot_player.shoot_pl(board)
print("************************************************************")
