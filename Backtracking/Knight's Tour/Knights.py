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
