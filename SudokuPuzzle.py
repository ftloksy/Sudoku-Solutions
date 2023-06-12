import Square
import Helper

class SudokuPuzzle:
  def __init__(self):
    self.thePuzzle = [[Square.Square() for i in range(9)] for j in range(9)];

  def setGivens(self, x, y, number):
    self.thePuzzle[y][x].setGiven(number)

  # Later, Please handle here. find has anything method call here.
  def getPuzzle(self):
    puzzle = []
    for row in self.thePuzzle:
      theRow = []
      for square in row:
        theRow.append(square.getGiven())
      puzzle.append(theRow)
    return puzzle

  def getPuzzleObj(self):
    return self.thePuzzle

  def getColumn(self, i):
    column = []
    for r in self.getPuzzle():
      column.append(r[i])
    return column

  def getGrids(self, x, y):
    startXLocation = x * 3
    endXLocation = x * 3 + 3
    startYLocation = y * 3
    endYLocation = y * 3 + 3
    grids = []
    for r in self.getPuzzle()[startYLocation:endYLocation]:
        grids.extend( r[startXLocation:endXLocation] )
    return grids

  def updatePossibleNumbers(self):
    for y in range(9):
      for x in range(9):
        if self.getPuzzle()[y][x] == 0:

          squareRelation = [
              self.getGrids(int(x/3), int(y/3)),
              self.getPuzzle()[y],
              self.getColumn(x)
          ]

          possibleNumbers = Helper.oneToNineArray()

          for numberList in squareRelation:
            possibleNumbers = Helper.dropExistNumbers(
              possibleNumbers, numberList)

          self.getPuzzleObj()[y][x].setPossibleNumber(possibleNumbers)
    return [[],[],[]]

  def setPossibleNumber(self, x, y, numbers):
    if not self.thePuzzle[y][x].sureThis():
      self.thePuzzle[y][x].setPossibleNumber(numbers)