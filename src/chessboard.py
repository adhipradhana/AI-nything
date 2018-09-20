from random import randint
from chesspiece import Rook, Bishop, Queen, Knight
from chessboard_error import ChessBoardFullError, ChessBoardPositionError

class ChessBoard:
    def __init__(self):
        """
            TODO:
        """
        self.grid = [[None for j in range(8)] for i in range(8)]
        self.list = []

    def __str__(self):
        """
            TODO:
        """
        self.print()

    def create_rook(self, color):
        """
            TODO:
        """
        if self.list.count < 64:
            new_x = randint(0, 63)
            new_y = randint(0, 63)
            while self.grid[new_x][new_y] is not None:
                new_x = randint(0, 63)
                new_y = randint(0, 63)
            r = Rook(new_x, new_y, color)
            self.grid[new_x][new_y] = color
            self.list.append(r)
        else:
            raise ChessBoardFullError("ChessBoard full")

    def create_bishop(self, color):
        """
            TODO:
        """
        if self.list.count < 64:
            new_x = randint(0, 63)
            new_y = randint(0, 63)
            while self.grid[new_x][new_y] is not None:
                new_x = randint(0, 63)
                new_y = randint(0, 63)
            b = Bishop(new_x, new_y, color)
            self.grid[new_x][new_y] = color
            self.list.append(b)
        else:
            raise ChessBoardFullError("ChessBoard full")
    
    def create_queen(self, color):
        """
            TODO:
        """
        if self.list.count < 64:
            new_x = randint(0, 63)
            new_y = randint(0, 63)
            while self.grid[new_x][new_y] is not None:
                new_x = randint(0, 63)
                new_y = randint(0, 63)
            q = Queen(new_x, new_y, color)
            self.grid[new_x][new_y] = color
            self.list.append(q)
        else:
            raise ChessBoardFullError("ChessBoard full")
    
    def create_knight(self, color):
        """
            TODO:
        """
        if self.list.count < 64:
            new_x = randint(0, 63)
            new_y = randint(0, 63)
            while self.grid[new_x][new_y] is not None:
                new_x = randint(0, 63)
                new_y = randint(0, 63)
            k = Knight(new_x, new_y, color)
            self.grid[new_x][new_y] = color
            self.list.append(k)
        else:
            raise ChessBoardFullError("ChessBoard full")

    def print(self):
        """
            Prints the chessboard.
        """
        pass

    def cost(self):
        """
            Returns list/tuple of cost of current state of the board
            (number of defenses, number of attacks)
        """
        pass

    def seek_cost(self, piece, x, y):
        """
            Returns list/tuple of cost if a piece P is moved to position x, y
            (number of defenses, number of attacks)
        """
        pass

    def move(self, piece, x, y):
        """
            Moves piece to the new position.
            raises ChessBoardPositionError if position is invalid
        """
        pass

    

    