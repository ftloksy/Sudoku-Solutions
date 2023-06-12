class Square:
  def __init__(self):
    self.isGiven = False
    self.possibleNumber = []
    self.sureNumber = 0
    self.possibleNumberLong = 0
  def setGiven(self, number):
    self.isGiven = True
    self.sureNumber = number
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
    if self.checkGiven:
      return self.sureNumber
    else:
      return 0
  def getPossibleNumber(self):
    return self.possibleNumber
  def getLongPossibleNumber(self):
    return self.possibleNumberLong
  
  def sureThis(self):
    if self.sureNumber != 0:
      return True
    return False