# This is solution that I thought
def palindrome(maxNum, minNum):
  num = maxNum
  jnum = maxNum
  result = 0
  while num > minNum:
    while jnum > minNum:
      multi  = num * jnum
      if (isPalindrome(multi) and result < multi):
        result = multi
      jnum -= 1
    num -= 1
    jnum = num  # this line is important
  return result

def isPalindrome(num):
  return str(num) == str(num)[::-1]

if __name__ == '__main__':
  print palindrome(99, 9)
  print palindrome(999, 99)

  # amazong idea from internet
  print max(a*b for a in range(100,1000) for b in range(a,1000) if str(a*b) == str(a*b)[::-1])