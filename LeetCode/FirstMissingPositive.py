"""
Leetcode 41: https://leetcode.com/problems/first-missing-positive/
"""
class Solution:
    def least_missing_positive(self, nums):
        n = len(nums)
        # 1st loop to remove irrelevant numbers
        for i in range(n):
            if nums[i] < 0: #or nums[i] > n:
                nums[i] = 0
        
        # 2nd: Assign all existing positive numbers in the correct index and assign an opposite number, 2 -> -2
        for i in range(n):
            if (0 <= abs(nums[i]) - 1) and (abs(nums[i]) - 1 < n):
                if nums[abs(nums[i]) - 1] > 0:
                    nums[abs(nums[i]) - 1] = (-1)*nums[abs(nums[i]) - 1]
                elif nums[abs(nums[i]) - 1] == 0:
                    nums[abs(nums[i]) - 1] = (-1)* (n + 1)

        # 3rd scan: the first index with a positive number will be the missing positive 
        for i in range(n):
            if nums[i] >= 0:
                return i + 1

        return n + 1

#arr = [2, 1, 9, 7, 3, 11, 4]
arr = [1, 2, 0]
arr = [100000, 3, 4000, 2, 15, 1, 99999]
sol = Solution()
target = 9
print(sol.least_missing_positive(arr))