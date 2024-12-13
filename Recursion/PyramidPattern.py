"""
Printing Pyramid Patterns using Recursion
"""

# Print a row of n *
def print_patternrow(k):
    if not(k):
        return 
    
    print("*", end=' ')

    print_patternrow(k - 1)

# Print the trianglar pattern
def pyramid_pattern(n, i):
    if not(n):
        return 
    
    print(' ' * int(n), end = '')
    print_patternrow(i)
    print()

    pyramid_pattern(n - 1, i + 1)

if __name__ == '__main__':
    n = 9
    pyramid_pattern(n, 1)