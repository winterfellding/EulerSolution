sumOfSquare = 0
squareOfSum = 0
sum1 = 0
for i in range(1, 101, 1):
    sumOfSquare += i ** 2
    sum1 += i
squareOfSum = sum1 ** 2
print squareOfSum - sumOfSquare
