# Find the nth row of the Pascal triangle

"""
1. Using Binomial Coefficient C(n, k) = n!/(k! (n - k)!)
    Naive implementation using recursion based on the formula
    C(n, k) = C(n - 1, k - 1) + C(n - 1, k)
    - Time complexity: 
"""

def recursive_nCk(n, k):    
    if k > n:
        return 0
    
    if k == 0 or k == n:        
        return 1
    
    return recursive_nCk(n - 1, k - 1) + recursive_nCk(n - 1, k)


def pascal_triangle(n):

    for i in range(n + 1):
        pt = []
        for j in range(i + 1):
            pt.append(recursive_nCk(i, j))
        s = ' '.join(str(x) for x in pt)
        print(s.center(4*n, ' '))
    return pt 

# Using Dynamic Programming with optimized memory 
def pascal_triangle_dp(n):
    dp = [0]*(n + 1)

    dp[0] = 1
    for i in range(n + 1):
        for j in range(i, 0, -1):
            dp[j] = dp[j] + dp[j - 1]            
        s = ' '.join(str(item) for item in dp if item > 0)
        print(s.center(4*n, ' '))
    return dp 

if __name__ == '__main__':
    n = 10
    print("\n", n, "th row of Pascal Triangle is: ", pascal_triangle(n))