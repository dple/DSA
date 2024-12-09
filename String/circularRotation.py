# Check all possible permutations
# Complexity: O(n^2)
def is_circular_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    
    for _ in range(len(s1)):
        if s1 == s2:
            return True
        s2 = s2[1:] + s2[0]
    
    return False

# Using built-in function 
def is_circular_rotation2(s1, s2):
    s1 += s1
    return s2 in s1

# Using KMP algorithm
def is_circular_rotation3(s1, s2):
    return


