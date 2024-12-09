import numpy as np

def is_all_1_matrix(mat):
    n = len(mat)
    for i in range(n):
        for j in range(n):
            if mat[i][j] != 1:
                return False
    
    print(mat.view())

    return True

# Complexity: O(n*m*min(n, m))
def largest_square_submatrix(mat):
    n, m = len(mat), len(mat[0])
    m_min = min(n, m)
    for i in range(m_min, 1, -1):
        for j in range(n - i + 1):
            for  k in range(m - i + 1):
                if is_all_1_matrix(mat[j: j + i, k: k + i]):
                    return i
    
    return 0

if __name__ == '__main__':
    matrix = np.array([
         [0, 1, 1, 0, 1],
        [1, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0]
    ])

    print(largest_square_submatrix(matrix))