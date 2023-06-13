# Set the Sudoku puzzle broad 
# and find that broad's solution.
# I know the setGivens is very hard 
# for common using. 
# Maybe I will add the web interface for version 2.
import SudokuValidator
import SudokuPuzzle
import Helper

def setSudokuPuzzle():
  sudokuPuzzle = SudokuPuzzle.SudokuPuzzle()
  sudokuPuzzle.setGivens(0, 0, 5)
  sudokuPuzzle.setGivens(1, 0, 3)
  sudokuPuzzle.setGivens(0, 1, 6)
  sudokuPuzzle.setGivens(1, 2, 9)
  sudokuPuzzle.setGivens(2, 2, 8)
    
  sudokuPuzzle.setGivens(4, 0, 7) 
  sudokuPuzzle.setGivens(3, 1, 1)
  sudokuPuzzle.setGivens(4, 1, 9)
  sudokuPuzzle.setGivens(5, 1, 5)
    
  sudokuPuzzle.setGivens(7, 2, 6)
    
  sudokuPuzzle.setGivens(0, 3, 8)
  sudokuPuzzle.setGivens(0, 4, 4)
  sudokuPuzzle.setGivens(0, 5, 7)
    
  sudokuPuzzle.setGivens(4, 3, 6)
  sudokuPuzzle.setGivens(3, 4, 8)
  sudokuPuzzle.setGivens(5, 4, 3)
  sudokuPuzzle.setGivens(4, 5, 2)
    
  sudokuPuzzle.setGivens(8, 3, 3)
  sudokuPuzzle.setGivens(8, 4, 1)
  sudokuPuzzle.setGivens(8, 5, 6)
    
  sudokuPuzzle.setGivens(1, 6, 6)
    
  sudokuPuzzle.setGivens(3, 7, 4)
  sudokuPuzzle.setGivens(4, 7, 1)
  sudokuPuzzle.setGivens(5, 7, 9)
  sudokuPuzzle.setGivens(4, 8, 8)
    
  sudokuPuzzle.setGivens(6, 6, 2)
  sudokuPuzzle.setGivens(7, 6, 8)
  sudokuPuzzle.setGivens(8, 7, 5)
  sudokuPuzzle.setGivens(7, 8, 7)
  sudokuPuzzle.setGivens(8, 8, 9)

  return sudokuPuzzle
    
    # Error case for test.
    # sudokuPuzzle.setGivens(8, 8, 7)
    
puzzle = setSudokuPuzzle()

sudokuValidator = SudokuValidator.IsVaild(puzzle)
if ( sudokuValidator.getTestedResult() ):
  print("-------- The Puzzle is vaild. ----------")

  puzzle.findSolution()

  for row in puzzle.getGivenPuzzle():
    print("     {}".format(row))

  print("------------ The Solution --------------")
  for row in puzzle.getPuzzle():
    print("     {}".format(row))