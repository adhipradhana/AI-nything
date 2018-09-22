from src.chessboard import ChessBoard
from src.chesspiece import Color
from src.util import parser
from src.algorithms import hill_climbing
# import src.chessboard

f = ChessBoard()
f.init_map("input.txt")
f.print()
print(f.cost())
hill_climbing(f)
# f.create_rook(Color.WHITE)
# f.create_bishop(Color.BLACK)
# f.print()
# print(f.cost())
# f.show_list()