"""
Leetcode 3046
https://leetcode.com/problems/split-the-array/description/
"""
from collections import Counter

class Solution:
    def split_array(self, nums: list[int]) -> bool:
        counter = Counter(nums)

        for c in counter.values():
            if c > 2:
                return False
            
        return True

sol = Solution()
nums = [1,1,2,2,3,2]

print(sol.split_array(nums))