import numpy as np 

def is_subgrid(mat):    
    k = len(mat)
    for i in range(k):
        if mat[0][i] != 'X' or mat[k - 1][i] != 'X' or mat[i][0] != 'X' or mat[i][k - 1] != 'X':
            return False
    
    print(mat.view())
    return True

def largest_square_subgrid(mat):
    n = len(mat)    
    for i in range(n, 2, -1):        
        for j in range(n - i + 1):
            for k in range(n - i + 1):
                if is_subgrid(mat[j:j + i, k: k + i]):                         
                    return i
    return 1

if __name__ == '__main__':
    ttt = np.array([
            ['X', 'O', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'O', 'X', 'O'],
            ['X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'O', 'O']
    ])

    print(largest_square_subgrid(ttt))