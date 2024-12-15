import math 


# Naive implementation using recursion based on the formula
#   C(n, k) = C(n - 1, k - 1) + C(n - 1, k)
def recursive_nCk(n, k):
    #if k > n // 2: 
    #    k = n - k
    print("n = ", n, "k = ", k)
    if k > n:
        return 0
    
    if k == 0 or k == n:        
        return 1
    
    return recursive_nCk(n - 1, k - 1) + recursive_nCk(n - 1, k)


# Using Dynamic Programming to avoid redundant calculation as in the recursive method
def nCk_util(n, k, nemo):    
    print("n = ", n, "k = ", k)
    if k > n:
        return 0
    
    if k == 0 or k == n:
        nemo[n][k] = 1
        return nemo[n][k]

    
    if nemo[n][k] != 0:
        return nemo[n][k]
    
    nemo[n][k] = nCk_util(n - 1, k - 1, nemo) + nCk_util(n - 1, k, nemo)

    return nemo[n][k]

# Dynamic Programming with memorization and recursive calls
# Time O(n*k), Space O(n*k)
def  dp_nCk(n, k):
    if k > n // 2: 
        k = n - k

    nemo = [[0 for _ in range(k + 1)] for _ in range(n + 1)]   

    return nCk_util(n, k, nemo)

# Dynamic Programming with bottom-up approach
# Time O(n*k), Space O(n*kk)
def dp_nCk_bottom_up(n, k):
    if k > n // 2: 
        k = n - k

    nemo = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            print("i = ", i, "j = ", j)
            if j == 0 or j == i:
                nemo[i][j] = 1
            
            else:
                nemo[i][j] = nemo[i - 1][j - 1] + nemo[i - 1][j]

    return nemo[n][k]


# DP with optimized memory using Pascal's triangle
# Time O(n*k), Space O(k)
def dp_nCk_optimized(n, k):
    
    dp = [0 for _ in range(k + 1)]

    # C(n, 0) = 1
    dp[0] = 1

    for i in range(1, n + 1):    
        for j in range(min(i, k), 0, -1):        
            dp[j] = dp[j] + dp[j - 1]
            print(dp[j], end=' ')

        print()
    
    return dp[k]

# Compute nCk using factorial and a table storing previous results 
def factorial_util(n, nemo):
    if n <= 1:        
        return 1
    
    if nemo[n] != -1:        
        return nemo[n]
    
    nemo[n] = n*factorial_util(n - 1, nemo)
    
    return nemo[n]

def factorial_nCk(n, k):
    nemo = [-1]*(n + 1)

    return factorial_util(n, nemo)/(factorial_util(k, nemo) * factorial_util(n - k, nemo))

# Wrap function 
def nCk(n, k):
    return dp_nCk_optimized(n, k)


if __name__ == '__main__':
    n = 5
    k = 3
    print("Combinations of ", k, " over ", n, " is: ", int(nCk(n, k)))