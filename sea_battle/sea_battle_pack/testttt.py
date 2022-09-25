import mod_ships
import mod_board
import shoot_player
import shoot_enemy

board = mod_board.BoardClass()
ship = mod_ships.Ship()

# mod_ships.pos_rand_en(board)
mod_ships.pos_rand_pl(board)

shoot_enemy.shoot_en(board)
print("************************************************************")
shoot_enemy.shoot_en(board)
print("************************************************************")
shoot_enemy.shoot_en(board)
print("************************************************************")
shoot_enemy.shoot_en(board)
print("************************************************************")


