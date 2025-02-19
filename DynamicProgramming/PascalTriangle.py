# Find the nth row of the Pascal triangle
def dp_nth_row_pascal_optimized(n):
    # Using Bottom-up Dynamic Programming (Tabulation) with optimized memory 
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
    print("\n", n, "th row of Pascal Triangle is: ", dp_nth_row_pascal_optimized(n))