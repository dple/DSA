"""
Catalan numbers satisfy the following recursive formula: 
C(0) = 1, C(1) = 1
C(n) = sum_{i = 0}^{n - 1}  C(i) x C(n - i - 1)
"""
def recursive_catalan(n):
    if n <= 1:
        return 1
    
    sum = 0
    for i in range(n):
        sum += recursive_catalan(i) * recursive_catalan(n - i - 1)
    
    return sum 

# Find nth Catalan number by using dynamic programming 
def catalan(n):
    if n <= 1:
        return 1
    
    cat = [0] * (n + 1)
    cat[0] = 1
    cat[1] = 1 

    for i in range(2, n + 1):
        for j in range(i):
            cat[i] += cat[j] * cat[i - j - 1]
            
    return cat[n]

if __name__ == '__main__':
    n = 5
    print(n, "th Calatan number is (recursive): ", recursive_catalan(n))
    print(n, "th Calatan number is (dynamic programming): ", catalan(n))
