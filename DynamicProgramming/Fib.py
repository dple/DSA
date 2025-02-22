"""
Compute the n_th element of the Fibonacci sequence 
"""

class Solution:
    def nth_fib(self, n):
        # 1st approach using recursion. Time complexity 0(2^n). Space 0(n)
        if n == 0 or n == 1:
            return 1
        
        return self.nth_fib(n - 1) + self.nth_fib(n - 2)
    
    def dp_fib_memo_util(self, n, memo):
        if n == 0 or n == 1:
            return 1
        if memo[n] != -1:
            return memo[n]
        
        return self.dp_fib_memo_util(n - 1, memo) + self.dp_fib_memo_util(n - 2, memo)

    def dp_fib_memo(self, n):
        # Using Top-Down Dynamic Programming or Memoization. Time complexity 0(n). Space 0(n) 
        memo = [-1] * (n + 1)       # memo likes a cache that stores all Fib solutions already computed
        
        return self.dp_fib_memo_util(n, memo)


    def dp_fib_tabu(self, n):
        # Using Bottom up dynamic programming or Tabulation.Time complexity 0(n). Space 0(n) 
        dp = [1, 1] + [0] * (n - 1)      # array storing solutions in order  

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
    
    def dp_fib_tabu_optimized(self, n):
        # Optimizing memory used in Tabulation. Time complexity 0(n). Space 0(1) 
        prev, cur = 1, 1
        for _ in range(2, n + 1):
            prev, cur = cur, prev + cur
        
        return cur

sol = Solution()
n = 10
print(n, "th element of the Fibonacci sequence (Recursion):", sol.nth_fib(n))
print(n, "th element of the Fibonacci sequence (Memoization):", sol.dp_fib_memo(n))
print(n, "th element of the Fibonacci sequence (Tabulation):", sol.dp_fib_tabu(n))
print(n, "th element of the Fibonacci sequence (Optimized Tabulation):", sol.dp_fib_tabu_optimized(n))