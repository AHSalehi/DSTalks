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

    def checkRightMove(self):
        width = self.map.getWidth()
        nextPos = Pos(self.current.row, self.current.col+1)
        return nextPos.col != (width - 1) and (self.map.getChar(nextPos) == '_' or self.map.getChar(nextPos) == 'D')

    def checkLeftMove(self):
        width = self.map.getWidth()
        nextPos = Pos(self.current.row, self.current.col - 1)
        return nextPos.col != 0 and (self.map.getChar(nextPos) == '_' or self.map.getChar(nextPos) == 'D')

    def checkDownMove(self):
        height = self.map.getHeight()
        nextPos = Pos(self.current.row + 1, self.current.col)
        return nextPos.row != (height - 1) and (self.map.getChar(nextPos) == '_' or self.map.getChar(nextPos) == 'D')

    def checkUpMove(self):
        height = self.map.getHeight()
        nextPos = Pos(self.current.row - 1, self.current.col)
        return nextPos.row != 0 and (self.map.getChar(nextPos) == '_' or self.map.getChar(nextPos) == 'D')

    def getActionList(self):
        return self.actionList

    def addActionList(self, action: str):
        self.actionList.append(action)

    def searchInThread(self, newPos: Pos):
        for pos in self.thread:
            if pos == newPos:
                return True
        return False

    def addPosToThread(self, newPos: Pos):
        if self.searchInThread(newPos):
            self.thread.append(newPos)
