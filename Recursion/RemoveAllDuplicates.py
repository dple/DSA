"""
Recursively remove all adjacent duplicates (https://www.geeksforgeeks.org/recursively-remove-adjacent-duplicates-given-string/)

Given a string S, the task is to remove all its adjacent duplicate characters recursively.

Input: S = “geeksforgeek”
Output: “gksforgk”
Explanation: g(ee)ksforg(ee)k -> gksforgk


Input: S = “abccbccba”
Output: ““
Explanation: ab(cc)b(cc)ba->abbba->a(bbb)a->aa->(aa)->”” (empty string)
"""

def is_nonadjacent_deuplicates(s):
    n = len(s)
    if n <= 1:
        return True
    
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
        
    return True

def remove_adjacent_duplicates(s):
    n = len(s)
    if n <= 1:
        return s
    i = 0

    while i < (len(s) - 1):
        j = i + 1
        while (j < len(s)) and (s[j] == s[i]):            
            j += 1
        if j > i + 1:
            s = s[:i] + s[j:]
        
        i += 1
        
    return s 

"""
Using recursion
- Time complexity O(n^2)
- Space complexity O(n)
"""
def remove_all_adjacent_duplicates(s):
    n = len(s)
    
    if n <= 1 or is_nonadjacent_deuplicates(s):
        return s
    
    else: 
        s = remove_adjacent_duplicates(s)
        return remove_all_adjacent_duplicates(s)


"""
Using list and a copy string to avoid modifying the original string
"""
def remove_all_adjacent_util(s, n):
    k = 0       # keep track new string
    i = 0       # index of current character under consideration

    while i < n:

        if (i < n - 1) and s[i] == s[i + 1]:
            while (i < n - 1) and s[i] == s[i + 1]:
                i += 1
        else:
            s[k] = s[i]
            k += 1
        
        i += 1
    
    s = s[:k]   # Get a new copy of string without duplicated adjacents

    if k != n:
        s = remove_all_adjacent_util(list(s), k)
    
    return s 

def remove_all_adjacent(s):
    s = list(s)
    
    return ''.join(remove_all_adjacent_util(s, len(s)))


if __name__ == '__main__':
    s = "abccbccba" #"geeksforgeek"

    print(remove_all_adjacent(s))
