"""
Leetcode 74
https://leetcode.com/problems/search-a-2d-matrix/
"""
class Solution:
    def linear_search(self, matrix, target) -> bool:
        # Scan and compare one by one element from beginning until found or the end if not found
        # Complexity 0(n*m)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i - 1][j] == target:
                    return True                
        
        return False

    def binary_search(self, matrix: list[list[int]], target: int) -> bool:
        # Perform a binary search in the entire matrix. Complexity 0(log(n*m))
        n, m = len(matrix), len(matrix[0])
        start, end = 0, n * m - 1
                
        while end >= start:
            mid = (end + start) // 2
            i, j = mid // m, mid % m
            if matrix[i][j] == target:
                return True
            elif (matrix[i][j] > target): 
                end = mid - 1
            else:
                start = mid + 1
        
        return False
    
    def binary_search_optimized(self, matrix: list[list[int]], target: int) -> bool:        
        # Perform two binary searches
        # Complexity: 0(log m) + 0(log n)
        # 1st binary search: performed in the first column to determine the right row
        n, m = len(matrix), len(matrix[0])
        top, bottom = 0, n - 1
        while top >= bottom:
            mid = (top + bottom) // 2            
            if matrix[mid][0] == target:
                return True
            elif (matrix[mid][0] > target): 
                bottom = mid - 1
            else:
                top = mid + 1
        
        # 2nd binary search: performed in the right row
        left, right = 0, m - 1

        while (left <= right):
            mid = (left + right) // 2
            if matrix[top][mid] == target:
                return True
            elif (matrix[top][mid] > target): 
                right = mid - 1
            else:
                left = mid + 1

        
        return False


    
sol = Solution()
#matrix = [[1], [3]]
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(sol.linear_search(matrix, target))
print(sol.binary_search(matrix, target))
print(sol.binary_search_optimized(matrix, target))