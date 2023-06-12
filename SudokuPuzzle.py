import OneToNineTester

class SudokuPuzzle:
  def __init__(self):
    self.thePuzzle = [[0 for i in range(9)] for j in range(9)];

  def setGivens(self, x, y, number):
    self.thePuzzle[y][x] = number

  def getPuzzle(self):
    return self.thePuzzle

  def getColumn(self, i):
    column = []
    for r in self.thePuzzle:
      column.append(r[i])
    return column

  def getGrids(self, x, y):
    startXLocation = x * 3
    endXLocation = x * 3 + 3
    startYLocation = y * 3
    endYLocation = y * 3 + 3
    grids = []
    for r in self.thePuzzle[startYLocation:endYLocation]:
        grids.extend( r[startXLocation:endXLocation] )
    return grids

  def getNextZero(self):
    for i in range(9):
      for j in range(9):
        if self.thePuzzle == 0:
          return (i, j)