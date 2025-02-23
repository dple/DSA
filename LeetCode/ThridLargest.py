"""
Leetcode 414: https://leetcode.com/problems/third-maximum-number/
"""

class Solution:
    def third_largest_number(self, nums: list[int]) -> int:
        if nums == []:
            return None
        
        first, second, third = float('-inf'), float('-inf'), float('-inf')

        for i in range(len(nums)):
            if nums[i] > first:
                third, second, first = second, first, nums[i]
            elif nums[i] < first and nums[i] > second:
                third, second = second, nums[i]
            elif nums[i] < second and nums[i] > third:
                third = nums[i]
        if third != float('-inf'):
            return third
        else:
            return first

sol = Solution()
nums = [3, 2, 3, 2,1]# [1, 14, 2, 16, 10, 20]
print("Third largest number in array:", sol.third_largest_number(nums))

