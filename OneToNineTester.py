# This is the Tester tools class.
# It will need pass needTest <array> for testing.
# It will do two tests, 
# 
# allItemIsBetweenOneToNine : this will check needTest
# every items is between 1-9 ,
#
# allItemIsUniqueNumber : this test will check every 
# items is unique. No two items has same number.
class Tester:
  def __init__(self, needTest):
    self.thisResult = True
    self.needTest = needTest
    self.allItemsIsBetweenOneToNine()
    self.allItemsIsUniqueNumbers()

  def allItemsIsBetweenOneToNine(self):
    for i in self.needTest:
      if i > 9 or i < 0:
        self.thisResult = False
  
  def allItemsIsUniqueNumbers(self):
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