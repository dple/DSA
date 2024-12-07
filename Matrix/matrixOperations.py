
def search(mat, x):
    rows, cols = len(mat), len(mat[0])

    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == x:
                return True
    
    return False

if __name__ == '__main__':
    mat = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

    print(search(mat, 3))