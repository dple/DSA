"""
Given a string, find the length of longest palindromic sub-string by using Recursion
"""

import time 
def maxi(x, y) :
    if x > y :
        return x
    else :
        return y
    
def is_palindrome(s):    
    s1 = s[::-1]
    if s == s1:
        return True
    else:
        return False

def recursive_palindrome(s, start, end, count):
        
    if start > end:
        return count 
    if start == end:
        return (count + 1)
    
    if s[start] == s[end]:
        count += 2
        recursive_palindrome(s, start + 1, end - 1, count + 2)

        return max(count, max(recursive_palindrome(s, start + 1, end, 0), recursive_palindrome(s, start, end - 1, 0)))        
        

    return max(recursive_palindrome(s, start + 1, end, 0), recursive_palindrome(s, start, end - 1, 0))

def recursive_palindrome1(s):
    if len(s) <= 1:
        return len(s)
    
    if is_palindrome(s):
        #print(s)
        return len(s)
    else: 
        return maxi(recursive_palindrome1(s[1:]), recursive_palindrome1(s[:-1]))

def longest_palindromic_substr(strn):
    
    # Utility function call
    k = len(strn) - 1
    res = recursive_palindrome(strn, 0, k, 0)
    #res = recursive_palindrome1(strn)    
    return res 

if __name__ == '__main__':
    s = "aaaabbaaiTopiNonAvevanoNipotiIguess"
    #s = "aaaabbaa"    
    s = s.lower()
    start = time.time()    
    print(longest_palindromic_substr(s))
    end = time.time()
    print("Running time is: ", (end - start), " seconds")
    

