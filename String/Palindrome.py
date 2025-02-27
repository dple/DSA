
"""
Palindrome is a string that read from left to right is equal to the string read from right to left. 

For example: By ignoring Upper or lower letters, "iTopiNonAvevanoNipoti" is a Palidrome 
"""
# Scan the string. Time O(len(s)). Space: O(1)
def isPalindrome(s):
    s1 = ''
    for c in s:
        s1 = c + s1
    
    if s == s1:
        return True
    else:
        return False

# Slightly better by scan half string 
def isPalindrome1(s):
    l = len(s)
    for i in range(int(l/2)):
        if s[i] != s[l - i - 1]:
            return False
    return True 

# Same complexity by using two pointers techniques 
def isPalindrome_twopointers(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False 
        left += 1
        right -= 1
    
    return True

# Using reverted string. Time O(1). Space: O(1)
def isPalindrome2(num):

    s = str(num)
    s1 = s[::-1]
    
    if s == s1:
        return True
    else:
        return False


if __name__ == "__main__":

    #s = "iTopiNonAvevanoNipoti"
    s = "racecar"
    s = s.lower()

    if (isPalindrome_twopointers(s)):
        print(s, " is a Palindrome string")
    else:
        print(s, " is NOT a Palindrome string")