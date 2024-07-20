from time import sleep


class Pos:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.status = False

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def getPos(self):
        return tuple((self.row, self.col))

    def getStatus(self):
        return self.status


class ChessBoard: # Constraints : Chess board is a square board
    def __init__(self, N: int):
        self.n = N
        self.map = [['_' for j in range(8)] for i in range(8)]

    def getStat(self, pos: Pos):
        return self.map[pos.row][pos.col]

    def mapSize(self):
        return self.n



