def square_of_sum_minus_sum_of_square(number):
    sum_of_square = 0
    square_of_sum = 0
    sum1 = 0
    for i in range(1, number + 1, 1):
        sum_of_square += i ** 2
        sum1 += i
    square_of_sum = sum1 ** 2
    return square_of_sum - sum_of_square
print square_of_sum_minus_sum_of_square(100)
