import mod_board
import mod_ships

board = mod_board.BoardClass()

mod_ships.pos_rand_en(board)
mod_ships.pos_rand_pl(board)
board.board_print()
