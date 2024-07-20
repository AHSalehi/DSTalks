from time import sleep


class Pos:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def getPos(self):
        return tuple((self.row, self.col))



class ChessBoard: # Constraints : Chess board is a square board
    def __init__(self, N: int):
        self.n = N
        self.map = [['_' for j in range(N)] for i in range(N)]

    def getStat(self, pos: Pos):
        return self.map[pos.row][pos.col]

    def mapSize(self):
        return self.n

    def printMap(self):
        for row in self.map:
            for cell in row:
                print(cell, end=' ')
            print()

    def setChar(self, pos: Pos, char: str):
        self.map[pos.row][pos.col] = char



def find_next_move(moveNumber, current: Pos, board: ChessBoard):
    mapSize = board.mapSize()
    row_delta = [2, 1, -1, -2, -2, -1, 1, 2]
    col_delta = [-1, -2, -2, -1, 1, 2, 2, 1]

    if moveNumber == mapSize*mapSize:
        return True
    for move in range(0, 8): # a single knight has only 8 possible moves
        new_row = current.row + row_delta[move]
        new_col = current.col + col_delta[move]
        if (new_row < 0 or new_row >= mapSize) or (new_col < 0 or new_col >= mapSize):
            continue
        if board.getStat(Pos(new_row, new_col)) != '_':
            continue

        board.setChar(Pos(new_row, new_col), str(moveNumber + 1))
        # print("----------------------------------------------")
        # board.printMap()
        # sleep(2.5)
        if find_next_move(moveNumber + 1, Pos(new_row, new_col), board):
            return True
        board.setChar(Pos(new_row, new_col), '_')

    return False




def solve(init_pos: Pos, N: int):
    board = ChessBoard(N)
    board.setChar(init_pos, '1')

    if find_next_move(1, init_pos, board):
        board.printMap()
    else:
        print("No move anymore. :x")




solve(Pos(0, 0), 8)
