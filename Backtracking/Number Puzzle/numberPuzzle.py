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