"""
Generate all possible combinations of N pairs of parenthesis using backtracking method
For example: 
Input: N = 3
Output: ((())), (()()), (())(), ()(()), ()()()
"""
N = 3

class Solution:
    def parenthesis_util(self, num_open, num_close, results, parenthesis):
        if num_open == num_close == N:
            results.append(''.join(parenthesis))
        
        if num_open < N:
            parenthesis.append('(')
            self.parenthesis_util(num_open + 1, num_close, results, parenthesis)
            parenthesis.pop()

        if num_close < num_open:
            parenthesis.append(')')
            self.parenthesis_util(num_open, num_close + 1, results, parenthesis)
            parenthesis.pop()

    def parenthesis(self):
        results = []
        parenthesis = []

        self.parenthesis_util(0, 0, results, parenthesis)

        return results
    
sol = Solution()
print(sol.parenthesis())


