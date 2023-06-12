import SudokuValidator
import SudokuPuzzle

def oneToNineArray():
  a = []
  for i in range(1, 10):
    a.append(i)
  return a

def dropExistNumbers(possibleNumbers, existNumbers):
  for number in existNumbers:
    if number != 0:
      for p in possibleNumbers:
        if p == number:
          possibleNumbers[p-1] = 0
  return possibleNumbers

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
  print("The Puzzle is vaild.")

possibleNumbers = oneToNineArray()

print("Number: {}".format(possibleNumbers))
nextZero = puzzle.getNextZero()
print("Next Zero: {}".format(nextZero));
for givenNumbers in nextZero:
  possibleNumbers = dropExistNumbers(possibleNumbers, givenNumbers)

print("Possible Number: {}".format(possibleNumbers))