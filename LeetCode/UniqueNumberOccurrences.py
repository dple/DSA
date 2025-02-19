"""
Given an array of integers, return True if the number of occurrences of each value in the array is unique or False otherwise.

For ex: 
Input: [1, 2, 2, 1, 1, 3]
Return: True (as occurrences of '1' is 3, '2' is 2, and '3' is 1)

Input: [1, 2]
Return: False (as both '1' and '2' occur 1 time)
"""
from collections import Counter

class Solution:
    def unique_number_occurrences(self, arr):
        # Method 1: Using dictionary
        dict = {}
        for x in arr:
            if x in dict:
                dict[x] += 1
            else:
                dict[x] = 1
        
        s = set(dict.values())

        if len(s) == len(dict):
            return True
        else:
            return False
        
    def unique_number_occurrences1(self, arr):
        # Using counter 
        c = Counter(arr)
        """
        s = set(c.values())        
        if len(s) == len(c):
            return True
        else:
            return False
        """
        s = set()
        for v in c.values():
            if v in s:
                return False
            else:
                s.add(v)
        return True
    
sol = Solution()
arr = [1, 2, 2, 1, 1, 3, 3]
print(sol.unique_number_occurrences1(arr))