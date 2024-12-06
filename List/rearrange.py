# Rearrange an array such that arr[i] = i

"""
Input: L[] = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
Output: [-1, 1, 2, 3, 4, -1, 6, -1, -1, 9]
Explanation: In range 0 to 9, all except 0, 5, 7 and 8 are present. Hence, we print -1 instead of them.
"""

# Using linear search whose complexity is O(n), hence complexity of rearrange will be O(n^2)
def rearrange_searching(L):
    res = []
    for i in range(len(L)):
        if i in L:
            res.append(i)
        else:
            res.append(-1)

    return res

# Sort then insert. Complexity: O(n log n)
def rearrange_sorting(L):
    res = []

    L.sort()

    for e in L:
        if e == -1:
            res.append(-1)
        else:
            res.insert(e, e)

    return res

# Complexity: O(n)
def rearrange_replacing(L):
    res = [-1]*len(L)

    for e in L:
        if e != -1:
            res[e] = e
    
    return res

if __name__ == '__main__':
    L = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]

    print("Rearrange array: ", rearrange_replacing(L))
