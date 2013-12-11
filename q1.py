def isMultiple3Or5(num):
  return num % 3 == 0 or num % 5 == 0

def sum(num):
  sum = 0
  for i in range(num):
    if isMultiple3Or5(i):
      sum += i
  return sum

if __name__ == '__main__':
  print sum(1000)
