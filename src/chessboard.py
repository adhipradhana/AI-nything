from random import randint
from .chesspiece import Rook, Bishop, Queen, Knight, Color, PieceType, index_valid
from .chessboard_error import ChessBoardFullError, ChessBoardPositionError

class ChessBoard:
    """ ChessBoard class """
    def __init__(self):
        """ Initializes a chessboard """
        self.grid = [[None for j in range(8)] for i in range(8)]
        self.list = []

    def __str__(self):
        """ Prints the chessboard trough print() function """
        self.print()

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

    def print(self):
        """ Prints the chessboard """
        temp_grid = [['.' for j in range(8)] for i in range(8)]
        characterize = {
            PieceType.BISHOP: 'B',
            PieceType.ROOK: 'R',
            PieceType.QUEEN: 'Q',
            PieceType.KNIGHT: 'K',
        }
        for chesspiece in self.list:
            temp_grid[chesspiece.y][chesspiece.x] = characterize[chesspiece.chesspiece_type]
            if chesspiece.color == Color.BLACK: 
                temp_grid[chesspiece.y][chesspiece.x] = temp_grid[chesspiece.y][chesspiece.x].lower()
        print("-"*17)
        for row in reversed(temp_grid):
            print("|" + ("|").join(row) + "|")
            print("-"*17)

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
                    if chesspiece == piece:
                        chesspiece.x = x
                        chesspiece.y = y
                        break
            else:
                raise ChessBoardPositionError("Position occupied")
        else:
            raise ChessBoardPositionError("Position invalid")

    

    