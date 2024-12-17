"""
1. Recursive approach
"""
def binary_search_util(arr, start, end, value):
    if start > end:
        return - 1
    
    mid = (start + end)//2
    if arr[mid] == value:
        return mid 
    
    if arr[mid] > value:
        return binary_search_util(arr, start, mid - 1, value)
    else:
        return binary_search_util(arr, mid + 1, end, value)
    

def binary_search(arr, value):
    return binary_search_util(arr, 0, len(arr) - 1, value)


'''
2. Iterative approach 
'''
def iterative_binary_search(arr, value):
    i, j = 0, len(arr) - 1

    while i < j:
        mid = (i + j) // 2
        if arr[mid] == value:
            return mid 
        if arr[mid] > value:
            j = mid - 1
        else:
            i = mid + 1
    
    return -1


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    value = 9
    print(binary_search(arr, value))
    print(iterative_binary_search(arr, value))
