from src.chessboard import ChessBoard
from src.chesspiece import Color
from src.util import parser
from src.algorithms import simulated_annealing
# import src.chessboard

f = ChessBoard()
f.init_map("input.txt")
simulated_annealing(f)
# f.print()
# f.move(f.list[1], 0, 0)
# f.print()
# f.move(f.list[0], 7, 7)
# f.print()
# f.move(f.list[0], 0, 0)
# f.print()
# print(f.cost())
# f.create_rook(Color.WHITE)
# f.create_bishop(Color.BLACK)
# f.print()
# f.show_list()