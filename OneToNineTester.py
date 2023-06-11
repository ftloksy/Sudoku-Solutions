class Tester:
  def __init__(self, needTest):
    self.thisResult = True
    self.needTest = needTest
    self.allItemIsBetweenOneToNine()
    self.allItemIsUniqueNumbers()

  def allItemIsBetweenOneToNine(self):
    for i in self.needTest:
      if i > 9 or i < 0:
        self.thisResult = False
  
  def allItemIsUniqueNumbers(self):
    for i in self.needTest:
      if i != 0:
        hasMatch = 0
        for j in self.needTest:
          if i == j:
            hasMatch += 1
        if hasMatch > 1:
          self.thisResult = False

  def getResult(self):
    return self.thisResult