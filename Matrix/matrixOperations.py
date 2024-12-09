def print_mat(s, mat):
    print(s)
    rows, cols = len(mat), len(mat[0])    
    print("[")
    for i in range(rows):
        print("  [", end= ' ')
        for j in range(cols):
            print(mat[i][j], end=' ')
        print("]")
    print("]")

def search(mat, x):
    rows, cols = len(mat), len(mat[0])

    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == x:
                return True
    
    return False

def transpose(mat):
    rows, cols = len(mat), len(mat[0])    
    res = [[0] * rows for _ in range(cols)] 

    for i in range(rows):
        for j in range(cols):
            res[j][i] = mat[i][j]                    
            
    return res

def rotate90(mat):
    rows, cols = len(mat), len(mat[0])
    res = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            res[cols - j - 1][i] = mat[i][j]

    return res

def rotate180(mat):
    n = len(mat)

    if n != len(mat[0]):
        print("Requiring a square matrix!")
        return 
    
    #res = [[0] * n for _ in range(n)]

    for i in range(n // 2):            
        for j in range(n):
            temp = mat[i][j]            
            mat[i][j] = mat[n - i - 1][n - j - 1]
            mat[n - i - 1][n - j - 1] = temp
    
    
    if (n & 1) == 1:  # Rotate the middle row
        m = n // 2        
        for j in range(n // 2):
            temp = mat[m][j]            
            mat[m][j] = mat[m][n - j - 1]
            mat[m][n - j - 1] = temp
    
    return mat 

# Check if two arrays are circular rotation of each other
# Convert array to string 
def is_circular_rotation_string(arr1, arr2):
    s1 = ''.join(map(str, arr1))
    s2 = ''.join(map(str, arr2))

    if len(s1) != len(s2):
        return False
    
    for _ in range(len(s1)): 
        if s1 == s2:
            return True
        
        s2 = s2[-1] + s2[:-1]

    return False

# Check if two arrays are circular rotation of each other
def is_circular_rotation(arr1, arr2):
    if arr1 is None or arr2 is None:
        return False
    
    if len(arr1) != len(arr2):
        return False
    n = len(arr1)
    
    for _ in range(n): 
        if arr1 == arr2:
            return True
        l = arr2[1:]
        l.insert(n - 1, arr2[0])
        arr2 = l
    
    return False


# Check if all rows of a matrix are circular rotations of each other
# Using hash set
def is_circular_rotations(mat):    
    
    for i in range(len(mat) - 1):                
        if not is_circular_rotation(mat[i], mat[i + 1]):
            return False
    
    return True

if __name__ == '__main__':
    mat = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

    mat2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    #print_mat("Matrix A: ", mat)


    #print(search(mat, 3))
    #print_mat("Transpose the matrix A: ", transpose(mat))
    #print_mat("Rotate 90 degree of A: ", rotate90(mat))
    #print_mat("Rotate 180 degree: ", rotate180(mat2))

    mat3 = [
        [1, 2, 3],
        [3, 1, 2],
        [2, 3, 1]
    ]
    print(is_circular_rotations(mat3))