import SudokuPuzzle
import OneToNineTester

class IsVaild:
  def __init__(self, puzzle):
    #self.sudokuPuzzle = SudokuPuzzle.SudokuPuzzle()
    self.sudokuPuzzle = puzzle
    self.testResult = True
    #self.setSudokuPuzzle()
    self.testRows()
    self.testColumns()
    self.testGrids()

  def testRows(self):
    puzzle = self.sudokuPuzzle.getPuzzle()
    for row in puzzle:
      print(row)
      if not OneToNineTester.Tester(row).getResult():
        self.testResult = False
    
  def testColumns(self):
    for i in range(9):
      column = self.sudokuPuzzle.getColumn(i)
      print("Colunm: {}".format( column ))
      if not OneToNineTester.Tester( column ).getResult():
        self.testResult = False
    
  def testGrids(self):
    for x in range(3):
      for y in range(3):
        print("Grids: {} - {}".format(x, y))
        grids = self.sudokuPuzzle.getGrids(x, y)
        print(grids)
        if not OneToNineTester.Tester( grids ).getResult():
          self.testResult = False
  
  def getTestedResult(self):
    return self.testResult

