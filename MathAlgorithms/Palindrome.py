
"""
Palindrome is a number that read from left to right is equal to the string read from right to left. 

For example: 1234567654321 is a Palidrome
"""

import math 

# Time O(log10(num)). Space: O(1)
def isPalindrome(n):

    l = math.floor(math.log10(n))

    for i in range(int(l / 2)):
        a = n % 10
        b = int(n / math.pow(10, (l - i)))
    

if __name__ == "__main__":

    num = 1234567654321

    if (isPalindrome(num)):
        print(num, " is a Palindrome number")
    else:
        print(num, " is NOT a Palindrome number")