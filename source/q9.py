# will find two answers
# one is 0 500 500 (throw away, not things we want)
# the other is 200 375 425, and the answer is 31875000
x, y, z = 0, 0, 1000

while z > 0:

    for x in range((1000 - z) // 2):
        y = 1000 - z - x
        if x ** 2 + y ** 2 == z ** 2:
            print(x, y, z)
            print(x * y * z)
            break
    z -= 1



