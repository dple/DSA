"""
Given a string, find the length of longest palindromic sub-string by using Recursion
"""

import time 
    
def is_palindrome(s):    
    s1 = s[::-1]
    if s == s1:
        return True
    else:
        return False


def recursive_palindrome(s, start, end, count):
    global no_calls 
    no_calls += 1
        
    if start > end:
        return count 
    
    if start == end:
        return (count + 1)
    
    if s[start] == s[end]:
        count = recursive_palindrome(s, start + 1, end - 1, count + 2)

        return max(count, max(recursive_palindrome(s, start + 1, end, 0), recursive_palindrome(s, start, end - 1, 0)))        
        

    return max(recursive_palindrome(s, start + 1, end, 0), recursive_palindrome(s, start, end - 1, 0))

# Better approach with less recursion calls
def recursive_palindrome1(s):
    global no_calls 
    no_calls += 1
    if len(s) <= 1:
        return len(s)
    
    if is_palindrome(s):
        #print(s)
        return len(s)
    else: 
        return max(recursive_palindrome1(s[1:]), recursive_palindrome1(s[:-1]))

def longest_palindromic_substr(strn):
    
    # Utility function call
    k = len(strn) - 1
    #res = recursive_palindrome(strn, 0, k, 0)
    res = recursive_palindrome1(strn)    
    return res 

if __name__ == '__main__':
    s = "aaiTopiNonAvevanoNipoti"
    #s = "abcaaaabbaaaa"    
    no_calls = 0
    s = s.lower()
    start = time.time()    
    print(longest_palindromic_substr(s))
    end = time.time()
    print("Running time is: ", (end - start), " seconds")
    print("Number of calls:", no_calls)
    

