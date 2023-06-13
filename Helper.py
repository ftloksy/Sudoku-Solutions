# Some helper function.
# oneToNineArray:
# It will create a array and the array
# has nine items inside
# [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
def oneToNineArray():
  a = []
  for i in range(1, 10):
    a.append(i)
  return a

# dropExistNumbers: 
# param:   possibleNumbers 
#            is a array, 
#            In Sudoku init time, it always is
#            a oneToNineArray.
#          
#          existNumbers
#             is a compared array group,
#             It maybe has three arrays:
#             a row, a column and a grids.
# If the existNumbers's items exists in possibleNumbers,
# let the possibleNumber's items to be Zero.
def dropExistNumbers(possibleNumbers, existNumbers):
  for number in existNumbers:
    if number != 0:
      for p in possibleNumbers:
        if p == number:
          possibleNumbers[p-1] = 0
  return possibleNumbers