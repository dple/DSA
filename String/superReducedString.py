"""
This script does cleaning a given string by removing two characters that are the same. For example:

Given: s = 'aaabcccddeeeffe'
Script will do 'aaabcccddeeeffe' -> 'abcccddeeeffe' -> 'abcddeeeffe' -> 'abceeeffe' -> 'abceffe' -> 'abcee' -> 'abc' 
Return: s = 'abc'
"""

import os

def superReducedString(s):
    '''
    The first method makes use of a predefined list and lookup if this happens in the string then remove. 
    This process repeats until none of 'predefined words' in the list is in the string. However, this 
    implementation limits to lower letters only.
    '''
        
    l = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll',
             'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']

    remove = 0
    while True:
        for c in l:
            if c in s:
                remove += 1
                s = s.replace(c, '')
        if remove == 0:
            break
        remove = 0

    if len(s) == 0:
        return 'Empty String'
    else:
        return s

def superReducedString1(s):
    '''
    The 2nd method has better performance and is more generic. It is applicable to any letters or special symbols.
    '''
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            s = s.replace(''.join([s[i], s[i + 1]]), '')
            i = i - 1 if i > 0 else 0
        i += 1

    if s[len(s) - 2] == s[len(s) - 1]:
        s = s.replace(''.join([s[len(s) - 2], s[len(s) - 1]]), '')

    if len(s) == 0:
        return 'Empty String'
    else:
        return s

if __name__ == '__main__':
    s = 'aaabcccddeeeffe'
    out = superReducedString(s)
    print(out)
    out1 = superReducedString(s)
    print(out1)
    
