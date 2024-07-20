from time import sleep


class Board:
    def __init__(self, N: int, map: list[list]): # Constraints : Board has square shape
        self.boardSize = N
        self.map = map

    def printMap(self):
        print("---------------------------------------------------")
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
        count = 0
        for row in self.map:
            for number in row:
                if number != ' ':
                    count += 1
        return self.findEmptyCell() != -1 and len(self.map) == len(self.map[0]) and count == self.boardSize**2 - 1

    def getChar(self, pos: tuple):
        return self.map[pos[0]][pos[1]]

    def setChar(self, pos: tuple, newChar):
        self.map[pos[0]][pos[1]] = newChar


def solve(board: Board):
    row_move = [1, -1, 0, 0]
    col_move = [0, 0, 1, -1]
    size = board.boardSize
    current = board.findEmptyCell()

    if not board.isCorrectBoard():
        return "Wrong map :x"

    if board.is_sorted() and (board.getChar((size - 1, size - 1)) == ' ' or board.getChar((0, 0)) == ' '):
        board.printMap()
        return True

    for i in range(4):
        next_row = current[0] + row_move[i]
        next_col = current[1] + col_move[i]
        if next_row < 0 or next_row >= board.boardSize or next_col < 0 or next_col >= board.boardSize:
            continue
        board.setChar(current, board.getChar((next_row, next_col)))
        board.setChar((next_row, next_col), ' ')
        board.printMap()
        if solve(board):
            return True

    return False




map = [
    [2, 1, 3],
    [4, 7, ' '],
    [8, 5, 6]
]

board = Board(3, map)
solve(board)
