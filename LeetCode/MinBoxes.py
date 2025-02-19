"""
Given two arrays, one is the number of apples and the another one is the list of boxes with capacities. Find the minimum of boxes used to contain all apples
For ex: 
[3, 4, 1, 7]
[3, 5, 8, 1]
"""

class Solution:
    def minimum_boxes(self, apples, capacities):
        total = sum(apples)
        capacities.sort(reverse=True)
        n_boxes = 0
        for box_size in capacities:
            if total > 0:
                total -= box_size
                n_boxes += 1
            else:
                return n_boxes
        
        if total > 0:
            return -1
        
        return n_boxes
    
apples = [3, 4, 1, 7]
capacities = [3, 5, 8, 1]

sol = Solution()
print("Required boxes:", sol.minimum_boxes(apples, capacities))
