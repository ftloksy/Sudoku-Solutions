class Square:
  def __init__(self):
    self.givenNumber = 0
    self.possibleNumber = []
  def setGiven(self, number):
    self.given = number
    self.possibleNumber = [number]
  def setPossibleNumber(self, numbers):
    self.possibleNumber = number
  def isGiven(self):
    if self.givenNumber:
      return True
    return False
  def getNumber(self):
    if self.givenNumber:
      return self.givenNumber
    if len(self.possibleNumber) == 1:
      return self.possibleNumber[0]
  def getPossibleNumber(self):
    return self.possibleNumber
  def getLongPossibleNumber(self):
    return len(self.possibleNumber)