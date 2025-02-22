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
    def naive_two_sum(self, nums: list[int], target: int) -> list[int]:
        # Naive approach by exhausively scanning the array find two numbers
        # Time: 0(n^2)
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return [-1, -1]
    
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        # Using hash map. Time complexity 0(n)
        h = {}
        
        for i, num in enumerate(nums):
            desired = target - num
            if desired in h:    # Lookup an item in hash map in O(1) time
                return [h[desired], i]
            h[num] = i

        return [-1, -1]     # Not found a pair

sol = Solution() 

nums = [2, 7, 11, 15]
target = 9
print("Naive solution", sol.two_sum(nums=nums, target=target))
print("Hash map solution", sol.two_sum(nums=nums, target=target))