# use Sieve of Eratosthenes to produce sequence of primary number
# if length is not enough, double the length of list
# answer is 104743
from math import sqrt, floor
init_len = 10000
def primary_count(length):
    li = []
    
    for i in range(length):
        li.append(i + 1)
    li[0] = 0
    for i in range(2, floor(sqrt(length)) + 1):
        if i % 2 == 1 or i == 2 :
            j = 2 * i - 1
            while j < len(li):
                li[j] = 0
                j += i
    count = 0

    for i in li:

        if i > 0:
            count += 1
        if count > 10000:
            print(i)
            break;
    return count

length = init_len
count = primary_count(length)
while count < 10001:
    print(length, count)
    length = length * 2
    count = primary_count(length)
    
