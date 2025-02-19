"""
Given an island map (represent by a 2D matrix of 1 and 0, 1 for land and 0 for water).
Task: Compute the perimeter of the island

Ex:
Input:
    0 1 0 0
    1 1 1 0
    0 1 0 0
    1 1 0 0

Output: 16
"""

class Solution:
    def island_perimeter(self, mat) -> int:
        perimeter = 0
        n = len(mat)
        m = len(mat[0])
        adjacents = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    perimeter += 4
                    for i_off, j_off in adjacents:
                        r, c = i + i_off, j + j_off
                        if 0 <= r < n and 0 <= c < m and mat[r][c]:
                            perimeter -=1
            
        return perimeter


sol = Solution()
mat = [
        [0, 1, 0, 0, 0], 
        [1, 1, 1, 0, 0], 
        [0, 1, 0, 0, 0], 
        [1, 1, 0, 0, 0]]

print("Perimeter:", sol.island_perimeter(mat))