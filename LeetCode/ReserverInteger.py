"""
Given an int, reverse it digits. 
For ex: 123 -> 321
"""
class Solution:
    def reverse(self, num: int):
        res = 0
        while num > 0:
            res = 10*res + (num % 10)
            num = num // 10
        
        return res
    
sol = Solution()
num = 123 
print(sol.reverse(num))