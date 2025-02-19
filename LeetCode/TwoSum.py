"""
Using HashMap to solve the two sum problem in a linear time O(n).

Two Sum problem: 
==================
Given an array of integers and a target number, find location of two numbers in the array s.t. their sum is equal to the targeted number

For ex:
Input: array= [2, 7, 11, 15], target = 9
Output: 0, 1
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