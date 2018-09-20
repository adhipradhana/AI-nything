class ChessBoardError(Exception):
    pass

class ChessBoardFullError(ChessBoardError):
    def __init__(self, message):
        self.message = message

class ChessBoardPositionError(ChessBoardError):
    def __init__(self, message):
        self.message = message
