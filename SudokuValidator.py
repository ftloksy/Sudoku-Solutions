# Check Sudoku puzzle is vaildator.
# use OneToNineTester
# testRows: test Sudoku puzzle's every rows.
# testColumns: test Sudoku puzzle's every columns.
# testGrids: test Sudoku puzzle's every grids.
# If three tests are pass, the Sudoku puzzle is vaild.
import SudokuPuzzle
import OneToNineTester

class IsVaild:
  def __init__(self, puzzle):
    self.sudokuPuzzle = puzzle
    self.testResult = True
    self.testRows()
    self.testColumns()
    self.testGrids()

  def testRows(self):
    puzzle = self.sudokuPuzzle.getPuzzle()
    for row in puzzle:
      if not OneToNineTester.Tester(row).getResult():
        self.testResult = False
    
  def testColumns(self):
    for i in range(9):
      column = self.sudokuPuzzle.getColumn(i)
      if not OneToNineTester.Tester( column ).getResult():
        self.testResult = False
    
  def testGrids(self):
    for x in range(3):
      for y in range(3):
        grids = self.sudokuPuzzle.getGrids(x, y)
        if not OneToNineTester.Tester( grids ).getResult():
          self.testResult = False
  
  def getTestedResult(self):
    return self.testResult