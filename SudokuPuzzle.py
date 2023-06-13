# This is the Sudoku Puzzle Class.
# It will handle the puzzle broad, rows, columns and grids.

import Square
import Helper

# A Common broad has 9 rows and every rows has 9 square.
#
# setGivens method Begin the game start the game hoster can use that
# to set the broad. at last hoster will set 17 square to special
# number and let the game just has only one solutions
#
# helperGetPuzzle method is a helper program,
# it will follow the getType to get the date from Sudoku puzzle's square.
#
# getPuzzle method is get the sure numbers 
# at set to a 2D puzzle array and return that array.
#
# getGivenPuzzle method is get the given numbers 
# at set to a 2D puzzle array and return that array.
#
# getPuzzleObj method will return whole puzzle broad,
# and user can access the very importmation from here.
# like every square's possibleNumbers 
#
# getColumn method, pass the square's x, 
# then method will return the square's x column.
#
# getGrids method, need pass the Grids's x, y location
# It will return the Grids array.
#
# updatePossibleNumbers method, it will update all square,
# that square isn't has sureNumber. 
# it will use Helper functions to find 
# What numbers can fill in the square 
# and keep the Sudoku puzzla still vaild.
# 
# findSolution method, it will find the Soduku puzzle's solution.
class SudokuPuzzle:
  def __init__(self):

    self.thePuzzle = [[Square.Square() for i in range(9)] for j in range(9)];

  def setGivens(self, x, y, number):
    self.thePuzzle[y][x].setGiven(number)
    
  def helperGetPuzzle(self, getType):
    puzzle = []
    for row in self.thePuzzle:
      theRow = []
      for square in row:
        if ( getType == "sure"):
          theRow.append(square.getSure())
        elif ( getType == "given" ):
          theRow.append(square.getGiven())
      puzzle.append(theRow)
    return puzzle

  def getPuzzle(self):
    return self.helperGetPuzzle("sure")

  def getGivenPuzzle(self):
    return self.helperGetPuzzle("given")

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

  def findSolution(self):
    while True:
      hasDoNotSureRow = 0
      self.updatePossibleNumbers()
      for row in self.getPuzzleObj():
        for square in row:
          if not square.sureThis():
            hasDoNotSureRow += 1
      if hasDoNotSureRow == 0:
        break