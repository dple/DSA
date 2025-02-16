"""
Using HashMap to solve the two sum problem in a linear time O(n)
"""
class Solution:
    def two_sum(self, nums, target):
        h = {}
        for i, num in enumerate(nums):
            h[num] = i
        
        for i, num in enumerate(nums):
            desired = target - num
            if desired in h and h[desired] != i:
                return i, h[desired]

sol = Solution() 

nums = [2, 7, 11, 15]
target = 9
print(sol.two_sum(nums=nums, target=target))