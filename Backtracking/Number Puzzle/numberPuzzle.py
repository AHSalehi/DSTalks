from time import sleep


class Board:
    def __init__(self, N: int, map: list[list]): # Constraints : Board has square shape
        self.boardSize = N
        self.map = map

    def printMap(self):
        for row in self.map:
            for number in row:
                print(number, end=' ')
            print()
        sleep(2.3)

    def moveRight(self, row, col): # row and col of empty cell of map
        temp = self.map[row][col]
        self.map[row][col] = self.map[row][col + 1]
        self.map[row][col + 1] = temp

    def moveLeft(self, row, col): # row and col of empty cell of map
        temp = self.map[row][col]
        self.map[row][col] = self.map[row][col - 1]
        self.map[row][col - 1] = temp

    def moveDown(self, row, col): # row and col of empty cell of map
        temp = self.map[row][col]
        self.map[row][col] = self.map[row + 1][col]
        self.map[row + 1][col] = temp

    def moveUp(self, row, col): # row and col of empty cell of map
        temp = self.map[row][col]
        self.map[row][col] = self.map[row - 1][col]
        self.map[row - 1][col] = temp

    def is_sorted(self):
        line = []
        for row in self.map:
            for number in row:
                if number != ' ':
                    line.append(number)
        base = line[:]
        base.sort()
        return base == line and self.map[self.boardSize - 1][self.boardSize - 1] == ' '

    def findEmptyCell(self):
        for i in range(len(self.map)):
            for j in range(len(self.map)):
                if self.map[i][j] == ' ':
                    return tuple((i, j))
        return -1

    def isCorrectBoard(self):
        return self.findEmptyCell() != -1 and len(self.map) == len(self.map[0])