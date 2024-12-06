# Give the list of distinct elements in a list

# Search if the current element is in the resulted list. Add if no
# Complexity O(n^2) (Unsorted search n for n elements)
def distinct(L):
    ret = []
    for e in L:
        if e not in ret:
            ret.append(e)
    return ret

# Sort the list first, then scan to add distinct elements
# Complexity O(n log n)
def distinct_sorting(L):
    ret = []

    L.sort()

    ret.append(L[0])
    for i in range(1, len(L)):

        if L[i] != L[i - 1]:
            ret.append(L[i])
    return ret 



# Best method using hash set
# Complexity O(n)
def distinct_elements(L):
    S = set(L)
    return list(S)

if __name__ == '__main__':
    L = [2, 4, 5, 2, 3, 6, 7, 5, 1, 7, 1]

    print("Distinct elements of L: ", distinct_sorting(L))