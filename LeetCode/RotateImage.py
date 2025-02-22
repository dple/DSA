"""
Leetcode 48: Rotate Image
https://leetcode.com/problems/rotate-image/description/
"""

class Solution:
    def rotate_image(self, image):
        n = len(image)
        assert n == len(image[0])
        # First step: Transpose the matrix 
        for i in range(n):
            for j in range(i):
                image[i][j], image[j][i] = image[j][i], image[i][j]

        # 2nd step: reflex elements over the vertical symmetric line
        for i in range(n):
            for j in range(n // 2):
                image[i][j], image[i][n - j - 1] = image[i][n - j - 1], image[i][j]

        return image
    
sol = Solution()

# = [[1,2,3],[4,5,6],[7,8,9]]
img = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

print("Rotated image:", sol.rotate_image(img))