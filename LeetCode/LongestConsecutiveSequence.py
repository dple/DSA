"""
Leetcode 128
https://leetcode.com/problems/longest-consecutive-sequence/description/
"""

class Solution:
    def longest_consecutive(self, nums: list[int]) -> int:
        # Using list. 1) sort list; 2) scan the list. Complexity: 0(nlog n)
        if nums == []: 
            return 0
        
        count = 1
        longest = 1
        nums = list(set(nums))
        nums.sort() 
        
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i] + 1:
                count += 1                
            else:                         
                longest = max(longest, count)                
                count = 1
                        
        longest = max(longest, count)                

        return longest
    
    def longest_consecutive_set(self, nums: list[int]) -> int:
        # Using set (contains unique numbers). Complexity 0(n) as lookup in a set is constant time 
        if nums == []: 
            return 0
        s = set(nums)
        nums = list(s)
        count = 1
        longest = 1
        
        
        for num in nums:
            if num in s and (num - 1) not in s:
                count = 1
                while num + 1 in s:                    
                    count += 1 
                    s.remove(num)
                    num += 1               
            
                if count > longest:
                    longest = count       
                
        
        return longest


sol = Solution()
nums = [0,3,7,2,5,8,4,6,0,1]
print("Longest consecutive sequence is:", sol.longest_consecutive(nums))
print("Longest consecutive sequence is (Using set):", sol.longest_consecutive_set(nums))