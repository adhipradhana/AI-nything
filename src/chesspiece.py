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
    def attack_defense(self, grid):
        pass


class Rook(ChessPiece):
    """
        TODO:
    """
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def attack_defense(self, grid):
        num_of_attacks = 0
        num_of_defenses = 0
        for x in range(self.x + 1, 8):
            if grid[x, self.y] != self.color:
                num_of_attacks += 1
                break
            elif grid[x, self.y] == self.color:
                num_of_defenses += 1
                break

        for x in range(self.x - 1, -1, -1):
            if grid[x, self.y] != self.color:
                num_of_attacks += 1
                break
            elif grid[x, self.y] == self.color:
                num_of_defenses += 1
                break

        for y in range(self.y + 1, 8):
            if grid[self.x, y] != self.color:
                num_of_attacks += 1
                break
            elif grid[self.x, y] == self.color:
                num_of_defenses += 1
                break

        for y in range(self.y - 1, -1, -1):
            if grid[self.x, y] != self.color:
                num_of_attacks += 1
                break
            elif grid[self.x, y] == self.color:
                num_of_defenses += 1
                break

class Bishop(ChessPiece):
    """
        TODO:
    """
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def attack_defense(self, grid):
        num_of_attacks = 0
        num_of_defenses = 0

        # lower left
        for delta in range(1, (self.x if self.x < self.y else self.y) + 1):
            if grid[self.x + delta, self.y + delta] != self.color:
                num_of_attacks += 1
                break
            elif grid[self.x + delta, self.y + delta] == self.color:
                num_of_defenses += 1
                break

        # lower right
        for delta in range(1, (7 - self.x if 7 - self.x < self.y else self.y) + 1):
            if grid[self.x + delta, self.y + delta] != self.color:
                num_of_attacks += 1
                break
            elif grid[self.x + delta, self.y + delta] == self.color:
                num_of_defenses += 1
                break

        # upper left
        for delta in range(1, (7 - self.x if 7 - self.x < 7 - self.y else 7 - self.y) + 1):
            if grid[self.x + delta, self.y - delta] != self.color:
                num_of_attacks += 1
                break
            elif grid[self.x + delta, self.y - delta] == self.color:
                num_of_defenses += 1
                break

        # upper left
        for delta in range(1, (self.x if self.x < 7 - self.y else 7 - self.y) + 1):
            if grid[self.x + delta, self.y - delta] != self.color:
                num_of_attacks += 1
                break
            elif grid[self.x + delta, self.y - delta] == self.color:
                num_of_defenses += 1
                break

class Queen(ChessPiece):
    """
        TODO:
    """
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def attack_defense(self, grid):
        num_of_attacks = 0
        num_of_defenses = 0

        # lower left
        for delta in range(1, (self.x if self.x < self.y else self.y) + 1):
            if grid[self.x + delta, self.y + delta] != self.color:
                num_of_attacks += 1
                break
            elif grid[self.x + delta, self.y + delta] == self.color:
                num_of_defenses += 1
                break

        # lower right
        for delta in range(1, (7 - self.x if 7 - self.x < self.y else self.y) + 1):
            if grid[self.x + delta, self.y + delta] != self.color:
                num_of_attacks += 1
                break
            elif grid[self.x + delta, self.y + delta] == self.color:
                num_of_defenses += 1
                break

        # upper left
        for delta in range(1, (7 - self.x if 7 - self.x < 7 - self.y else 7 - self.y) + 1):
            if grid[self.x + delta, self.y - delta] != self.color:
                num_of_attacks += 1
                break
            elif grid[self.x + delta, self.y - delta] == self.color:
                num_of_defenses += 1
                break

        # upper left
        for delta in range(1, (self.x if self.x < 7 - self.y else 7 - self.y) + 1):
            if grid[self.x + delta, self.y - delta] != self.color:
                num_of_attacks += 1
                break
            elif grid[self.x + delta, self.y - delta] == self.color:
                num_of_defenses += 1
                break

        # right
        for x in range(self.x + 1, 8):
            if grid[x, self.y] != self.color:
                num_of_attacks += 1
                break
            elif grid[x, self.y] == self.color:
                num_of_defenses += 1
                break

        # left
        for x in range(self.x - 1, -1, -1):
            if grid[x, self.y] != self.color:
                num_of_attacks += 1
                break
            elif grid[x, self.y] == self.color:
                num_of_defenses += 1
                break

        # up
        for y in range(self.y + 1, 8):
            if grid[self.x, y] != self.color:
                num_of_attacks += 1
                break
            elif grid[self.x, y] == self.color:
                num_of_defenses += 1
                break

        # down
        for y in range(self.y - 1, -1, -1):
            if grid[self.x, y] != self.color:
                num_of_attacks += 1
                break
            elif grid[self.x, y] == self.color:
                num_of_defenses += 1
                break

class Knight(ChessPiece):
    """
        TODO:
    """
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def attack_defense(self, grid):
        num_of_attacks = 0
        num_of_defenses = 0
        if index_valid(self.x + 2, self.y + 1):
            if self.color != grid[self.x + 2][self.y + 1]:
                num_of_attacks += 1
            else:
                num_of_defenses += 1

        if index_valid(self.x + 2, self.y - 1):
            if self.color != grid[self.x + 2][self.y - 1]:
                num_of_attacks += 1
            else:
                num_of_defenses += 1

        if index_valid(self.x - 2, self.y + 1):
            if self.color != grid[self.x - 2][self.y + 1]:
                num_of_attacks += 1
            else:
                num_of_defenses += 1

        if index_valid(self.x - 2, self.y - 1):
            if self.color != grid[self.x - 2][self.y - 1]:
                num_of_attacks += 1
            else:
                num_of_defenses += 1

        if index_valid(self.x + 1, self.y + 2):
            if self.color != grid[self.x + 1][self.y + 2]:
                num_of_attacks += 1
            else:
                num_of_defenses += 1

        if index_valid(self.x + 1, self.y - 2):
            if self.color != grid[self.x + 1][self.y - 2]:
                num_of_attacks += 1
            else:
                num_of_defenses += 1

        if index_valid(self.x - 1, self.y + 2):
            if self.color != grid[self.x - 1][self.y + 2]:
                num_of_attacks += 1
            else:
                num_of_defenses += 1

        if index_valid(self.x - 1, self.y - 2):
            if self.color != grid[self.x - 1][self.y - 2]:
                num_of_attacks += 1
            else:
                num_of_defenses += 1


