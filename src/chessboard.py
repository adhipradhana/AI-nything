from random import randint
import os

from .chesspiece import Rook, Bishop, Queen, Knight, Color, PieceType, index_valid
from .chessboard_error import ChessBoardFullError, ChessBoardPositionError
from .util import parser, get_terminal_width

rows, columns = os.popen('stty size', 'r').read().split()
rows, columns = int(rows), int(columns)

class ChessBoard:
    """ ChessBoard class """
    def __init__(self):
        """ Initializes a chessboard """
        self.grid = [[None for j in range(8)] for i in range(8)]
        self.list = []

    def __str__(self):
        """ Prints the chessboard trough print() function """
        self.print()

    def init_map(self, filename):
        self.grid = [[None for j in range(8)] for i in range(8)]
        self.list = []
        pieces = parser(filename)
        for piece in pieces:
            if piece[1] == 'KNIGHT':
                for _ in range(0, int(piece[2])):
                    self.create_knight(Color[piece[0]])
            elif piece[1] == 'ROOK':
                for _ in range(0, int(piece[2])):
                    self.create_rook(Color[piece[0]])
            elif piece[1] == 'QUEEN':
                for _ in range(0, int(piece[2])):
                    self.create_queen(Color[piece[0]])
            elif piece[1] == 'BISHOP':
                for _ in range(0, int(piece[2])):
                    self.create_bishop(Color[piece[0]])

    def create_rook(self, color):
        """ Creates a new Rook """
        if len(self.list) < 64:
            new_x = randint(0, 7)
            new_y = randint(0, 7)
            while self.grid[new_x][new_y] is not None:
                new_x = randint(0, 7)
                new_y = randint(0, 7)
            r = Rook(new_x, new_y, color)
            self.grid[new_x][new_y] = color
            self.list.append(r)
        else:
            raise ChessBoardFullError("ChessBoard full")

    def create_bishop(self, color):
        """ Creates a new Bishop """
        if len(self.list) < 64:
            new_x = randint(0, 7)
            new_y = randint(0, 7)
            while self.grid[new_x][new_y] is not None:
                new_x = randint(0, 7)
                new_y = randint(0, 7)
            b = Bishop(new_x, new_y, color)
            self.grid[new_x][new_y] = color
            self.list.append(b)
        else:
            raise ChessBoardFullError("ChessBoard full")
    
    def create_queen(self, color):
        """ Creates a new Queen """
        if len(self.list) < 64:
            new_x = randint(0, 7)
            new_y = randint(0, 7)
            while self.grid[new_x][new_y] is not None:
                new_x = randint(0, 7)
                new_y = randint(0, 7)
            q = Queen(new_x, new_y, color)
            self.grid[new_x][new_y] = color
            self.list.append(q)
        else:
            raise ChessBoardFullError("ChessBoard full")
    
    def create_knight(self, color):
        """ Creates a new Knight """
        if len(self.list) < 64:
            new_x = randint(0, 7)
            new_y = randint(0, 7)
            while self.grid[new_x][new_y] is not None:
                new_x = randint(0, 7)
                new_y = randint(0, 7)
            k = Knight(new_x, new_y, color)
            self.grid[new_x][new_y] = color
            self.list.append(k)
        else:
            raise ChessBoardFullError("ChessBoard full")

    def randomize(self):
        """ Randomizes the position of all Chesspieces """
        self.grid = [[None for j in range(8)] for i in range(8)]
        for chesspiece in self.list:
            new_x = randint(0, 7)
            new_y = randint(0, 7)
            while self.grid[new_x][new_y] is not None:
                new_x = randint(0, 7)
                new_y = randint(0, 7)
            self.grid[new_x][new_y] = chesspiece.color
            chesspiece.x = new_x
            chesspiece.y = new_y

    def print(self, centered=False):
        """ Prints the chessboard """
        temp_grid = [[' ' for j in range(8)] for i in range(8)]
        characterize = {
            Color.BLACK: {
                PieceType.BISHOP: '\u2657',
                PieceType.ROOK: '\u2656',
                PieceType.QUEEN: '\u2655',
                PieceType.KNIGHT: '\u2658',
            },
            Color.WHITE: {
                PieceType.BISHOP: '\u265d',
                PieceType.ROOK: '\u265c',
                PieceType.QUEEN: '\u265b',
                PieceType.KNIGHT: '\u265e',
            }
        }

        background = {
            "black": "\x1B[100m",
            "white": "\x1B[0;30;47m",
            "default": "\x1B[0m"
        }
        for chesspiece in self.list:
            i = chesspiece.y
            j = chesspiece.x
            if ((i + 1) * 8 + j + 1) % 2 == 0:
                if i % 2 == 0:
                    # Background white
                    if chesspiece.color == Color.BLACK:
                        temp_grid[chesspiece.y][chesspiece.x] = characterize[Color.WHITE][chesspiece.chesspiece_type]
                    else:
                        temp_grid[chesspiece.y][chesspiece.x] = characterize[Color.BLACK][chesspiece.chesspiece_type]
                else:
                    # Background black
                    if chesspiece.color == Color.BLACK:
                        temp_grid[chesspiece.y][chesspiece.x] = characterize[Color.BLACK][chesspiece.chesspiece_type]
                    else:
                        temp_grid[chesspiece.y][chesspiece.x] = characterize[Color.WHITE][chesspiece.chesspiece_type]
            else: 
                if i % 2 == 0:
                    # Background black
                    if chesspiece.color == Color.BLACK:
                        temp_grid[chesspiece.y][chesspiece.x] = characterize[Color.BLACK][chesspiece.chesspiece_type]
                    else:
                        temp_grid[chesspiece.y][chesspiece.x] = characterize[Color.WHITE][chesspiece.chesspiece_type]
                else:
                    # Background white
                    if chesspiece.color == Color.BLACK:
                        temp_grid[chesspiece.y][chesspiece.x] = characterize[Color.WHITE][chesspiece.chesspiece_type]
                    else:
                        temp_grid[chesspiece.y][chesspiece.x] = characterize[Color.BLACK][chesspiece.chesspiece_type]

        print()

        if centered:
            print(' ' * int((get_terminal_width() - 28) / 2), end="")

        print("   ", end="")
        for c in range(ord('a'), ord('h') + 1):
            print(" {} ".format(chr(c)), end="")
        print("   ")

        for i in range(7, -1, -1):
            if centered:
                print(' ' * int((get_terminal_width() - 28) / 2), end="")

            print(" {} ".format(i + 1), end="")
            for j in range(8):
                if ((i + 1) * 8 + j + 1) % 2 == 0:
                    if i % 2 == 0:
                        print(background["white"], end="")
                    else:
                        print(background["black"], end="")
                else: 
                    if i % 2 == 0:
                        print(background["black"], end="")
                    else:
                        print(background["white"], end="")
                print(" " + temp_grid[i][j] + " ", end="")
                print(background["default"], end="")
            print(" {} ".format(i + 1))

        if centered:
            print(' ' * int((get_terminal_width() - 28) / 2), end="")

        print("   ", end="")
        for c in range(ord('a'), ord('h') + 1):
            print(" {} ".format(chr(c)), end="")
        print("   ")

        print()
        

    def cost(self):
        """
            Returns list/tuple of cost of current state of the board
            (number of defenses, number of attacks)
        """
        total_defenses = 0
        total_attacks = 0
        for chesspiece in self.list:
            no_of_defenses, no_of_attacks = chesspiece.attack_defense(self.grid)
            total_attacks += no_of_attacks
            total_defenses += no_of_defenses
        
        return (total_defenses, total_attacks)

    def seek_cost(self, piece, x, y):
        """
            Returns list/tuple of cost if a piece P is moved to position x, y
            (number of defenses, number of attacks)
        """
        if index_valid(x, y):
            if self.grid[x][y] is None:
                total_defenses = 0
                total_attacks = 0
                for chesspiece in self.list:
                    if chesspiece == piece:
                        no_of_defenses, no_of_attacks = chesspiece.attack_defense(self.grid, x, y)
                    else:
                        no_of_defenses, no_of_attacks = chesspiece.attack_defense(self.grid)

                    total_attacks += no_of_attacks
                    total_defenses += no_of_defenses
                
                return (total_defenses, total_attacks)
            else:
                raise ChessBoardPositionError("Position occupied")
        else:
            raise ChessBoardPositionError("Position invalid")

    def move(self, piece, x, y):
        """
            Moves piece to the new position.
            raises ChessBoardPositionError if position is invalid
        """
        if index_valid(x, y):
            if self.grid[x][y] is None:
                for chesspiece in self.list:
                    # print(self.grid[x][y])
                    if chesspiece == piece:
                        # print("{} {} init".format(chesspiece.x,chesspiece.y))
                        self.grid[x][y] = chesspiece.color
                        self.grid[chesspiece.x][chesspiece.y] = None
                        chesspiece.x = x
                        chesspiece.y = y
                        break
            else:
                raise ChessBoardPositionError("Position occupied")
        else:
            raise ChessBoardPositionError("Position invalid")

    def print_pieces_location(self):
        for selected_piece in self.list:
            if selected_piece.chesspiece_type == PieceType.QUEEN:
                chesstype = 'QUEEN'
            elif selected_piece.chesspiece_type == PieceType.ROOK:
                chesstype = 'ROOK'
            elif selected_piece.chesspiece_type == PieceType.BISHOP:
                chesstype = 'BISHOP'
            else:
                chesstype = 'KNIGHT'

            if selected_piece.color == Color.WHITE:
                colortype = 'WHITE'
            else:
                colortype = 'BLACK'
            print('{} {} ({},{})'.format(chesstype, colortype, selected_piece.x, selected_piece.y))

    