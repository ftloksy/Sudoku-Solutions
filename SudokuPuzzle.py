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
    for y in range(9):
      for x in range(9):
        if self.thePuzzle[y][x] == 0:

#           print( "Grids: {}".format(self.getGrids(int(x/3), int(y/3))) )
#           print( "Row: {}".format( self.thePuzzle[y]) )
#           print( "Column: {}".format(self.getColumn(x)) )
# 
#           return (x, y, (int(x/3), int(y/3)))
          return [
              self.getGrids(int(x/3), int(y/3)),
              self.thePuzzle[y],
              self.getColumn(x)
          ]
    return [[],[],[]]