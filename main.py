from src.chessboard import ChessBoard
from src.chesspiece import Color
from src.util import parser
from src.algorithms import simulated_annealing
from src.algorithms import hill_climbing
from src.algorithms import genetic_algorithm
# import src.chessboard

# f = ChessBoard()
# f.init_map("input.txt")

exit = False
init = False
c = ChessBoard()
while not exit:
    print("Welcome to N-anything chess solver!!")
    print("Menu choice :")
    print("1. Init Chessboard")
    print("2. Hill Climbing")
    print("3. Simulated Annealing")
    print("4. Genetic Algorithm")
    print("5. Print Chessboard")
    print("6. Exit")
    choose = raw_input()
    if (choose == "1"):
        print("Masukkan nama file :")
        filename = raw_input()
        try:
            c.init_map(filename)
            init = True
        except e:
            print("Nama file salah!!")
    elif (choose == "2"):
        if init:
            hill_climbing(c)
    elif (choose == "3"):
        if init:
            simulated_annealing(c)
    elif (choose == "4"):
        if init:
            genetic_algorithm(c)
    elif (choose == "5"):
        if init:
            c.print()
    elif (choose == "6"):
        exit = True
# simulated_annealing(f)
# hill_climbing(f)
# genetic_algorithm(f)
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