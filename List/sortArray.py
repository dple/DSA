"""
We are given an array that contains 1 to n elements, our task is to sort this array in an efficient way. We are not allowed to simply copy the numbers from 1 to n.
Examples : 

Input : arr[] = {2, 1, 3};
Output : {1, 2, 3}


Input : arr[] = {2, 1, 4, 3};
Output : {1, 2, 3, 4} 

https://www.geeksforgeeks.org/sort-array-contain-1-n-values/
"""

# Using sort algorithm. Complexity: O(n log n)
def sort_sorting(L):
    L.sort()
    return L

# Complexity: O(n)
def linear_sort(L):
    i = 0

    while i < len(L):
        if L[i] == i + 1:
            i += 1
        else:
            temp = L[L[i] - 1]
            L[L[i] - 1] = L[i]
            L[i] = temp            
    
    return L


    

if __name__ == '__main__':
    L = [5, 2, 6, 7, 1, 4, 3]
    print("Sorted array: ", linear_sort(L))