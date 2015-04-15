# use Sieve of Eratosthenes to get the primary number,
# and plus them all

import math
length = 2000000
li = []
# init numbers
for i in range(length):
    li.append(i + 1)
print(len(li))
# 1 is not primary number
li[0] = 0
for i in range(2, math.floor(math.sqrt(length)) + 1):
    j = 2 * i - 1
    while j < length:
        li[j] = 0
        j += i
    
print(len(li))
res = 0

for ele in li:
    res += ele

print(res)
