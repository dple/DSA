"""
https://leetcode.com/problems/climbing-stairs/description/
"""

class Solution:
    def climbing_stairs(self, n):
        # Using a recursion approach. Time Complexity: O(2^n), Space: O(n)
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        two_back = self.climbing_stairs(n - 2)
        one_back = self.climbing_stairs(n - 1)

        return two_back + one_back
    

    def dp_climbing_stairs_memo(self, n):
        # Using Top-Down dynamic programming (Memorization)
        memo = [-1] * (n + 1)
        res = self.dp_climbing_stairs_memo_util(n, memo)
        
        return res

    def dp_climbing_stairs_memo_util(self, n, memo):
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # if the result for this subproblem is already computed then return it
        if memo[n] != -1:
            return memo[n]
                
        return self.dp_climbing_stairs_memo_util(n - 1, memo) + self.dp_climbing_stairs_memo_util(n - 2, memo)

    def dp_climbing_stairs_tabulation(self, n):
        # Using Bottom-up Dynamic programming approach. Time complexity O(n), Space O(n)
        dp = [0] * n

        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i -2]
        return dp[n - 1]

sol = Solution()
n = 10
print("Number of solutions (Recursion):", sol.climbing_stairs(n))
print("Number of solutions (Top-down DP):", sol.dp_climbing_stairs_memo(n))
print("Number of solutions (Bottom-up DP):", sol.dp_climbing_stairs_tabulation(n))
