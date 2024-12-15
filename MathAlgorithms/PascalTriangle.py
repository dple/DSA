# Find the nth row of the Pascal triangle
# Using Dynamic Programming with optimized memory 
def nth_row_pascal(n):
    dp = [0]*(n + 1)

    dp[0] = 1
    for i in range(n + 1):
        for j in range(i, 0, -1):
            dp[j] = dp[j] + dp[j - 1]
            #print(dp[j], end=' ')
        s = ' '.join(str(item) for item in dp if item > 0)
        print(s.center(4*n, ' '))
    return dp 

if __name__ == '__main__':
    n = 10
    print("\n", n, "th row of Pascal Triangle is: ", nth_row_pascal(n))