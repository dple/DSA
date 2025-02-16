"""
Given a sorted array, output an array of squares of elements, also sorted
Note: inputs could be negative and positive numbers. 

For example: 
Input: [-6, -3, 1, 2, 5]
Output: [1, 4, 9, 25, 36]
"""

class Solution:
    def squares_sorted_list(self, nums):
        '''
        Using the Two Pointers technique to solve the problem
        '''
        left, right = 0, len(nums) - 1
        res = []
        while left <= right:
            """
            Scan from both sides of the array. Append the bigger squares.
            Note: The bigger absolute value of the number will produce the BIGGEST square 
            in the remaining considered array, however the smaller may not produce the 
            SMALLEST square in the remaining considered array
            """
            if (abs(nums[left]) > abs(nums[right])):
                res.append(nums[left]**2)
                left += 1
            else:
                res.append(nums[right]**2)
                right -= 1
        return res[::-1]    # Invert to get a sorted array from smallest to biggest

sol = Solution()
nums = [-6, -3, 1, 2, 5]

print(sol.squares_sorted_list(nums=nums))