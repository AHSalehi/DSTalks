class Pos:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def getPos(self):
        return tuple((self.row, self.col))


class Maze:
    def __init__(self, map: list[list], width: int, height: int):
        self.map = map
        self.width = width
        self.height = height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def setChar(self, spcPos: Pos, newChar: str):
        self.map[spcPos.row][spcPos.col] = newChar

    def getChar(self, position: Pos):
        return self.map[position.row][position.col]


class Seeker:
    def __init__(self, initPos: Pos, maze: Maze):
        self.thread = [initPos]
        self.map = maze
        self.current = initPos
        self.actionList = []

    def getCurrentPos(self):
        return self.current


