
# Using string. Time O(log10(num)). Space: O(1)
def isPalindrome(num):

    s = str(num)
    s1 = ''
    for c in s:
        s1 = c + s1
    
    if s == s1:
        return True
    else:
        return False
    
# Using string. Time O(1). Space: O(1)
def isPalindrome1(num):

    s = str(num)
    s1 = s[::-1]
    # s1 = list(s) 
    # s1.reverse()
    # s1 = ''.join(s1)
    
    if s == s1:
        return True
    else:
        return False


if __name__ == "__main__":

    num = 1234567654321

    if (isPalindrome1(num)):
        print(num, " is a Palindrome number")
    else:
        print(num, " is NOT a Palindrome number")