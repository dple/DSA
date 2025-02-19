"""
https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/

Given an array of N distinct elements, find the minimum number of swaps required to sort the array.

Examples: 

Input: {4, 3, 2, 1}
Output: 2
Explanation: Swap index 0 with 3 and 1 with 2 to form the sorted array {1, 2, 3, 4}



Input: {1, 5, 4, 3, 2}
Output: 2, swap 2 <-> 5, and 3 <-> 4
"""

def min_swaps(L):
    states = [0] * len(L)    # array record visited elements
    no_swaps = 0
    #i = 0

    for i in range(len(L)):
        # If element e at position i is correct (i.e., e == i + 1) or if the position was visited, then skip
        if (L[i] == i + 1) or states[i]:   
            continue #state[i] ^= 1     i += 1

        else:            
            # Find a cycle            
            states[i] = 1
            cycle_size = 2          # Cycle is at least 2
            j = L[i] - 1            # get the correct position of L[i]
            states[j] = 1
            while L[j] != i + 1:
                j = L[j] - 1
                states[j] = 1
                cycle_size += 1

            no_swaps += cycle_size - 1
    
    return no_swaps
        
                

if __name__ == '__main__':
    L = [1, 5, 2, 3, 4]
    print("Minimum number of swaps is: ", min_swaps(L))