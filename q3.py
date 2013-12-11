import math

def biggestPrimerFactor(num):
  i = 2
  factor = 1
  sqrtNum = math.sqrt(num)
  while i <= sqrtNum:
    if num % i == 0:
      num = num / i
      factor = i
    else:
      i += 1
  return factor

if __name__ == '__main__':
  print biggestPrimerFactor(13195)
  print biggestPrimerFactor(600851475143)
  print biggestPrimerFactor(121)