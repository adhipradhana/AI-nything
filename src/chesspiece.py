from enum import Enum
from abc import ABC, abstractmethod

class PieceType(Enum):
    KNIGHT = 0
    BISHOP = 1
    ROOK = 2
    QUEEN = 3

class Color(Enum):
    """
        TODO:
    """
    WHITE = 0
    BLACK = 1

def index_valid(x, y):
    """
        TODO:
    """
    return x < 8 and x >= 0 and y < 8 and y >= 0

class ChessPiece(ABC):
    """
        TODO:
    """
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    @abstractmethod
    def attack_defense(self, grid, x, y):
        pass


class Rook(ChessPiece):
    """
        TODO:
    """
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.chesspiece_type = PieceType.ROOK

    def attack_defense(self, grid, curr_x=None, curr_y=None):
        curr_x = curr_x if curr_x is not None else self.x
        curr_y = curr_y if curr_y is not None else self.y

        num_of_attacks = 0
        num_of_defenses = 0
        for x in range(curr_x + 1, 8):
            if grid[x, curr_y] != self.color:
                num_of_attacks += 1
                break
            elif grid[x, curr_y] == self.color:
                num_of_defenses += 1
                break

        for x in range(curr_x - 1, -1, -1):
            if grid[x, curr_y] != self.color:
                num_of_attacks += 1
                break
            elif grid[x, curr_y] == self.color:
                num_of_defenses += 1
                break

        for y in range(curr_y + 1, 8):
            if grid[curr_x, y] != self.color:
                num_of_attacks += 1
                break
            elif grid[curr_x, y] == self.color:
                num_of_defenses += 1
                break

        for y in range(curr_y - 1, -1, -1):
            if grid[curr_x, y] != self.color:
                num_of_attacks += 1
                break
            elif grid[curr_x, y] == self.color:
                num_of_defenses += 1
                break

        return (num_of_defenses, num_of_attacks)

class Bishop(ChessPiece):
    """
        TODO:
    """
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.chesspiece_type = PieceType.BISHOP

    def attack_defense(self, grid, curr_x=None, curr_y=None):
        curr_x = curr_x if curr_x is not None else self.x
        curr_y = curr_y if curr_y is not None else self.y

        num_of_attacks = 0
        num_of_defenses = 0

        # lower left
        for delta in range(1, (curr_x if curr_x < curr_y else curr_y) + 1):
            if grid[curr_x + delta, curr_y + delta] != self.color:
                num_of_attacks += 1
                break
            elif grid[curr_x + delta, curr_y + delta] == self.color:
                num_of_defenses += 1
                break

        # lower right
        for delta in range(1, (7 - curr_x if 7 - curr_x < curr_y else curr_y) + 1):
            if grid[curr_x + delta, curr_y + delta] != self.color:
                num_of_attacks += 1
                break
            elif grid[curr_x + delta, curr_y + delta] == self.color:
                num_of_defenses += 1
                break

        # upper left
        for delta in range(1, (7 - curr_x if 7 - curr_x < 7 - curr_y else 7 - curr_y) + 1):
            if grid[curr_x + delta, curr_y - delta] != self.color:
                num_of_attacks += 1
                break
            elif grid[curr_x + delta, curr_y - delta] == self.color:
                num_of_defenses += 1
                break

        # upper left
        for delta in range(1, (curr_x if curr_x < 7 - curr_y else 7 - curr_y) + 1):
            if grid[curr_x + delta, curr_y - delta] != self.color:
                num_of_attacks += 1
                break
            elif grid[curr_x + delta, curr_y - delta] == self.color:
                num_of_defenses += 1
                break

        return (num_of_defenses, num_of_attacks)

class Queen(ChessPiece):
    """
        TODO:
    """
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.chesspiece_type = PieceType.QUEEN

    def attack_defense(self, grid, curr_x=None, curr_y=None):
        curr_x = curr_x if curr_x is not None else self.x
        curr_y = curr_y if curr_y is not None else self.y

        num_of_attacks = 0
        num_of_defenses = 0

        # lower left
        for delta in range(1, (curr_x if curr_x < curr_y else curr_y) + 1):
            if grid[curr_x + delta, curr_y + delta] != self.color:
                num_of_attacks += 1
                break
            elif grid[curr_x + delta, curr_y + delta] == self.color:
                num_of_defenses += 1
                break

        # lower right
        for delta in range(1, (7 - curr_x if 7 - curr_x < curr_y else curr_y) + 1):
            if grid[curr_x + delta, curr_y + delta] != self.color:
                num_of_attacks += 1
                break
            elif grid[curr_x + delta, curr_y + delta] == self.color:
                num_of_defenses += 1
                break

        # upper left
        for delta in range(1, (7 - curr_x if 7 - curr_x < 7 - curr_y else 7 - curr_y) + 1):
            if grid[curr_x + delta, curr_y - delta] != self.color:
                num_of_attacks += 1
                break
            elif grid[curr_x + delta, curr_y - delta] == self.color:
                num_of_defenses += 1
                break

        # upper left
        for delta in range(1, (curr_x if curr_x < 7 - curr_y else 7 - curr_y) + 1):
            if grid[curr_x + delta, curr_y - delta] != self.color:
                num_of_attacks += 1
                break
            elif grid[curr_x + delta, curr_y - delta] == self.color:
                num_of_defenses += 1
                break

        # right
        for x in range(curr_x + 1, 8):
            if grid[x, curr_y] != self.color:
                num_of_attacks += 1
                break
            elif grid[x, curr_y] == self.color:
                num_of_defenses += 1
                break

        # left
        for x in range(curr_x - 1, -1, -1):
            if grid[x, curr_y] != self.color:
                num_of_attacks += 1
                break
            elif grid[x, curr_y] == self.color:
                num_of_defenses += 1
                break

        # up
        for y in range(curr_y + 1, 8):
            if grid[curr_x, y] != self.color:
                num_of_attacks += 1
                break
            elif grid[curr_x, y] == self.color:
                num_of_defenses += 1
                break

        # down
        for y in range(curr_y - 1, -1, -1):
            if grid[curr_x, y] != self.color:
                num_of_attacks += 1
                break
            elif grid[curr_x, y] == self.color:
                num_of_defenses += 1
                break

        return (num_of_defenses, num_of_attacks)

class Knight(ChessPiece):
    """
        TODO:
    """
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.chesspiece_type = PieceType.KNIGHT

    def attack_defense(self, grid, curr_x=None, curr_y=None):
        curr_x = curr_x if curr_x is not None else self.x
        curr_y = curr_y if curr_y is not None else self.y

        num_of_attacks = 0
        num_of_defenses = 0
        if index_valid(curr_x + 2, curr_y + 1):
            if self.color != grid[curr_x + 2][curr_y + 1]:
                num_of_attacks += 1
            else:
                num_of_defenses += 1

        if index_valid(curr_x + 2, curr_y - 1):
            if self.color != grid[curr_x + 2][curr_y - 1]:
                num_of_attacks += 1
            else:
                num_of_defenses += 1

        if index_valid(curr_x - 2, curr_y + 1):
            if self.color != grid[curr_x - 2][curr_y + 1]:
                num_of_attacks += 1
            else:
                num_of_defenses += 1

        if index_valid(curr_x - 2, curr_y - 1):
            if self.color != grid[curr_x - 2][curr_y - 1]:
                num_of_attacks += 1
            else:
                num_of_defenses += 1

        if index_valid(curr_x + 1, curr_y + 2):
            if self.color != grid[curr_x + 1][curr_y + 2]:
                num_of_attacks += 1
            else:
                num_of_defenses += 1

        if index_valid(curr_x + 1, curr_y - 2):
            if self.color != grid[curr_x + 1][curr_y - 2]:
                num_of_attacks += 1
            else:
                num_of_defenses += 1

        if index_valid(curr_x - 1, curr_y + 2):
            if self.color != grid[curr_x - 1][curr_y + 2]:
                num_of_attacks += 1
            else:
                num_of_defenses += 1

        if index_valid(curr_x - 1, curr_y - 2):
            if self.color != grid[curr_x - 1][curr_y - 2]:
                num_of_attacks += 1
            else:
                num_of_defenses += 1

        return (num_of_defenses, num_of_attacks)


