import time
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

    def printMaze(self):
        for row in self.map:
            for item in row:
                print(item, end= ' ')
            print()


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
        return self.current.col != (width - 1) and (self.map.getChar(nextPos) == '_' or self.map.getChar(nextPos) == 'D')

    def checkLeftMove(self):
        width = self.map.getWidth()
        nextPos = Pos(self.current.row, self.current.col - 1)
        return self.current.col != 0 and (self.map.getChar(nextPos) == '_' or self.map.getChar(nextPos) == 'D')

    def checkDownMove(self):
        height = self.map.getHeight()
        nextPos = Pos(self.current.row + 1, self.current.col)
        return self.current.row != (height - 1) and (self.map.getChar(nextPos) == '_' or self.map.getChar(nextPos) == 'D')

    def checkUpMove(self):
        height = self.map.getHeight()
        nextPos = Pos(self.current.row - 1, self.current.col)
        return self.current.row != 0 and (self.map.getChar(nextPos) == '_' or self.map.getChar(nextPos) == 'D')

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
            self.thread.append(newPos)



def solve(seeker:Seeker, currentPos: Pos, maze: Maze):

    thread = seeker.thread

    if maze.getChar(seeker.current) == 'D':
        return True

    if seeker.current == currentPos and seeker.actionList != []:
        return False

    else:

        if seeker.checkRightMove():
            nextPos = Pos(seeker.current.row, seeker.current.col + 1)
            if seeker.searchInThread(nextPos):
                maze.setChar(nextPos, '◉')
                maze.setChar(seeker.current, '#')
                seeker.current = nextPos
            else:
                seeker.addPosToThread(nextPos)
                maze.setChar(seeker.current, '_')
                seeker.current = nextPos
                maze.setChar(nextPos, '◉')
            maze.printMaze()
            print("----------------------------------------")
            time.sleep(0.5)
            return solve(seeker, seeker.current, maze)


        elif seeker.checkDownMove():
            nextPos = Pos(seeker.current.row + 1, seeker.current.col)
            if seeker.searchInThread(nextPos):
                maze.setChar(nextPos, '◉')
                maze.setChar(seeker.current, '#')
                seeker.current = nextPos
            else:
                seeker.addPosToThread(nextPos)
                maze.setChar(seeker.current, '_')
                seeker.current = nextPos
                maze.setChar(nextPos, '◉')

            maze.printMaze()
            print("----------------------------------------")

            time.sleep(0.5)
            return solve(seeker, seeker.current, maze)


        elif seeker.checkLeftMove():
            nextPos = Pos(seeker.current.row, seeker.current.col - 1)
            if seeker.searchInThread(nextPos):
                maze.setChar(nextPos, '◉')
                maze.setChar(seeker.current, '#')
                seeker.current = nextPos
            else:
                seeker.addPosToThread(nextPos)
                maze.setChar(seeker.current, '_')
                seeker.current = nextPos
                maze.setChar(nextPos, '◉')


            maze.printMaze()
            print("----------------------------------------")
            time.sleep(0.5)
            return solve(seeker, seeker.current, maze)


        elif seeker.checkUpMove():
            nextPos = Pos(seeker.current.row - 1, seeker.current.col)
            if seeker.searchInThread(nextPos):
                maze.setChar(nextPos, '◉')
                maze.setChar(seeker.current, '#')
                seeker.current = nextPos
            else:
                seeker.addPosToThread(nextPos)
                maze.setChar(seeker.current, '_')
                seeker.current = nextPos
                maze.setChar(nextPos, '◉')


            maze.printMaze()
            print("----------------------------------------")
            time.sleep(0.5)
            return solve(seeker, seeker.current, maze)


        else:
            return False


map = [
    ['_', '_', '_', '_', '_'],
    ['#', '#', '_', '_', '#'],
    ['#', '_', '_', '#', '_'],
    ['_', '_', '#', '#', '#'],
    ['_', '_', '_', '_', 'D']
]

maze = Maze(map, 5, 5)
maze.printMaze()
seeker = Seeker(Pos(0, 0), maze)
solve( seeker ,Pos(0, 0), maze)