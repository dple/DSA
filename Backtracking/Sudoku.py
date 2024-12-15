N = 9
rows = [0] * N              # Bit masks for rows. Each element in rows represents a row. If the n^th bit is seted (bit = 1), the number n exists in the row
cols = [0] * N              # Same as rows
sub_grids = [0] * N         # Similar as rows for sub-grid
    

"""
1. Naive solution: try all possible combinations
"""

def is_safe(grid, col, row, num):
    # Check if the number exists in the row 
    for i in range(N):
        if grid[row][i] == num:
            return False 
        
    # Check if the number exists in the col
    for i in range(N):
        if grid[i][col] == num:
            return False 
    
    # Check if the number exists in the 3 x 3 sub-grid
    for i in range(3):
        for j in range(3):
            if grid[row - (row % 3) + i][col - (col % 3) + j] == num: 
                return False 
    
    return True 

def naive_sudoku(grid, row, col):
    
    if (row == N - 1) and (col == N):
        return True
    
    if col == N:
        row += 1
        col = 0

        
        
    # Try all possible number from 1 to 9
    for num in range(1, N + 1):
        if is_safe(grid, col, row, num):
            grid[row][col] = num 

            if naive_sudoku(grid, row, col + 1):
                return True
            
        grid[row][col] = 0

    return False


'''
2. Backtracking solution
'''
def find_next_cell(grid):    
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0:
                return [i, j]                
    return [-1, -1]

def backtracking_sudoku(grid):

    row, col = find_next_cell(grid)  # tracking the empty cell

    if  row == -1:      # No more empty cell
        return True 
    

    for num in range(1, N + 1):
        if is_safe(grid, col, row, num):
            grid[row][col] = num

            if backtracking_sudoku(grid):
                return True 
            
        grid[row][col] = 0 

    return False


'''
Bitmasks solution
'''
def get_subgrid(row, col):
    # There are 9 3x3 sub-grids (0 - 8)
    return int(row / 3) * 3 + int(col / 3)

'''
Initialize bit masks for rows, cols, and sub-grids
'''
def initialize_bitmasks(grid):
    for i in range(N):
        for j in range(N):
            rows[i] |= 1 << grid[i][j]
            cols[j] |= 1 << grid[i][j]
            sub_grids[get_subgrid(i, j)] |= 1 << grid[i][j]

def bitmask_is_safe(row, col, num):
    return not((rows[row] >> num) & 1) and \
        not((cols[col] >> num) & 1) and \
            not((sub_grids[get_subgrid(row, col)] >> num) & 1)


def bitmask_sudoku(grid, row, col):
    if (row == N - 1) and (col == N):
        return True
    
    if col == N:
        row += 1
        col = 0

    if grid[row][col] > 0:
        bitmask_sudoku(grid, row, col + 1)

    for num in range(1, N + 1):

        if is_safe(grid, col, row, num):
            grid[row][col] = num
            # Set bit for bit masks 
            rows[row] |= 1 << num 
            cols[col] |= 1 << num 
            sub_grids[get_subgrid(row, col)] |= 1 << num 

            if bitmask_sudoku(grid, row, col + 1):
                return True 
            
            # Unset bit masks
        rows[row] &= ~(1 << num) 
        cols[col] &= ~(1 << num) 
        sub_grids[get_subgrid(row, col)] &= ~(1 << num )
        grid[row][col] = 0
    
    return False


def solve_sudoku(grid):
    #return naive_suduku(grid, 0, 0)
    return backtracking_sudoku(grid)
    #initialize_bitmasks(grid)
    #return bitmask_sudoku(grid, 0, 0)

if __name__ == '__main__':
    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    
    if solve_sudoku(grid):
        for row in grid:
            print(*row)
    else:
        print("There is no solution!")