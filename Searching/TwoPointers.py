"""
Given a sorted array arr (sorted in ascending order) and a target, find if there exists any pair of elements (arr[i], arr[j]) such that 
their sum is equal to the target.

Input: arr[] = {10, 20, 35, 50}, target =70
Output:  Yes
Explanation : There is a pair (20, 50) with given target.
"""

'''
1. Naive approach
- Time complexity O(n^2). Space O(1)
'''
def naive_twosum(arr, sum):
    n = len(arr)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if (arr[i] + arr[j]) == sum:
                return True
            
    return False

"""
2. Binary search and hashing

"""
if __name__ == '__main__':
    arr = [10, 20, 30, 40, 50, 70]

    print(naive_twosum(arr, 70))