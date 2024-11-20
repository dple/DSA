import math 

# Naive implementation of Fibonacci by using recursion 
# This approach contains redundant calculations in which Fabonacci numbers will be re-calculated by different calls: nth_Fibanacci_recursion(n - 1) and nth_Fibanacci_recursion(n - 2)
# Time complexity: O(2^n)
# Space O(n)
def nth_Fibonacci_recursion(n):
    if n <= 1:
        return 1
    return nth_Fibonacci_recursion(n - 1) + nth_Fibonacci_recursion(n - 2)

# More efficient approach that uses a nemo table to store Fibonacci numbers calculated 
# Recursive implementation 
def nth_Fibonacci_util(n, nemo):
    if n <= 1:
        return 1
    
    # If nth number was calculated, just return it
    if nemo[n] != -1:
        return nemo[n]
    
    nemo[n] = nth_Fibonacci_util(n - 1, nemo) + nth_Fibonacci_util(n - 2, nemo)

    return nemo[n]

# Iterative implementation, more efficient than recursive 
# Time complexity O(n). Space O(1) 
def nth_iterative_Fibonacci(n):
    if n <= 1:
        return 1    
    
    a = 0
    b = 1
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    
    return c

# By using a nemo table, the time complexity reduce to O(n), Space O(n)
def nth_Fibonacci(n):
    # Initlize a nemo table of n + 1 elements whose value is -1
    nemo = [-1] * (n + 1)

    return nth_Fibonacci_util(n, nemo)


"""
Using matrix 

(1 1)^n-1       (F(n)       F(n - 1))
 1 0        =    F(n - 1)   F(n - 2)
"""
def multiply_matrix(mat1, mat2):
    mat = [[0, 0], [0, 0]]
    mat[0][0] = mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0]
    mat[0][1] = mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]
    mat[1][0] = mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0]
    mat[1][1] = mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1]

    return mat 

def nth_Fibonacci_matrix(n):
    if n <= 1:
        return 
    mat = [[1, 1], [1, 0]]
    base = mat 

    bit_pos = int(math.log(n, 2)) - 1
    while bit_pos >= 0:                
        bit = (n & (1 << bit_pos)) >> bit_pos        
        mat = multiply_matrix(mat, mat)
        
        if bit == 1:
            mat = multiply_matrix(mat, base)            

        bit_pos -= 1
    return mat[0][0]

if __name__ == '__main__':
    n = int(input("Provide a number n: ").strip())

    print("nth Fibonacci number is: ", nth_iterative_Fibonacci(n))
    print("nth Fibonacci number is: ", nth_Fibonacci_matrix(n - 1))