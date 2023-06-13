# This is square of Sudoku, every Sudoku has 9 x 9 square
# In this programming, every square is a class.
# If the square's number is given before the game start.
# Set the Object's isGiven attribute to True
# and set the sureNumber is the sudoku puzzle given.
# If the square haven't given before game start.
# program will check the square can fill what number
# and keep the sudoku puzzla is still vaild.
# and set the numbers to  possibleNumber.arrays.
# The possibleNumber will automate update by program.
# when the sudoku soluting.
# possibleNumberLong is use to store current possibleNumber
# has any items. update everytime when possibleNumber update.
# When the possibleNumberLong is 1, 
# ( Of course, someting the square just can assign only 
# one special number like 3, not two like 2 or 4 )
#  set the only one item
# in possibleNumber items to sureNumber.
class Square:
  def __init__(self):
    self.isGiven = False
    self.possibleNumber = []
    self.sureNumber = 0
    self.possibleNumberLong = 0

  def setGiven(self, number):
    self.isGiven = True
    self.sureNumber = number

  # Update the possibleNumber
  # and count the array's vaild long
  # and storage to posibleNumberLong
  # When the possibleNumberLong is 1,
  # storage the only one item to sureNumber.
  def setPossibleNumber(self, numbers):
    self.possibleNumber = numbers
    long = 0
    lastVaildNumber = 0
    for n in self.possibleNumber:
      if n != 0:
        long += 1
        lastVaildNumber = n
    if long == 1:
      self.sureNumber = lastVaildNumber
    self.possibleNumberLong = long

  def checkGiven(self):
    return self.isGiven

  def getSure(self):
    return self.sureNumber

  def getGiven(self):
    if self.checkGiven():
      return self.sureNumber
    else:
      return 0

  def getSure(self):
    return self.sureNumber

  def getPossibleNumber(self):
    return self.possibleNumber
  def getLongPossibleNumber(self):
    return self.possibleNumberLong
  
  def sureThis(self):
    if self.sureNumber != 0:
      return True
    return False