# Find the nth row of the Pascal triangle
# Using Dynamic Programming with optimized memory 
def nth_row_pascal(n):
    dp = [0]*(n + 1)

    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(i, 0, -1):
            dp[j] = dp[j] + dp[j - 1]
            print(dp[j], end=' ')
        print()
    return dp 

if __name__ == '__main__':
    n = 31
    print(n, "th row of Pascal Triangle is: ", nth_row_pascal(n))