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