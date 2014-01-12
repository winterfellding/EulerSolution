import math  

def numCheck(input, num):
        for i in range(num):
                if input % (i + 1) != 0:
                        return 0
        return 1

def minMulti(num):
    bigMul = num
    biggestNum = math.factorial(num)

    while num < biggestNum:
            if numCheck(num, bigMul) == 1:
                    print "The smallest number found is: ", num
                    break
            else:
                    num += bigMul

if __name__ == '__main__':
    minMulti(20) 
