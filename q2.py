def evenFibonacciSum(maxNum):
  sum = 0
  fibonacci = initializeFibonacci(maxNum)
  for number in fibonacci:
    if number % 2 == 0:
      sum += number
  return sum

def initializeFibonacci(maxNum):
  num1 = 1
  num2 = 2
  fibonacci = [num1, num2]
  #initial fibonacci number
  while num1 + num2 < maxNum:
    num1, num2 = num2, num1 + num2
    fibonacci.append(num2)
  return fibonacci

if __name__ == '__main__':
  print evenFibonacciSum(4000000)
