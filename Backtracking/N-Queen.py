"""
Solve N-queen problems using Backtracking (i.e., basically brute-force)
"""

"""
1. Naive recursive approach
    - Generate all possible permutations of [1, 2, 3, …, n] using Use backtracking
    - For each permutation, check if any two queens are placed on the same diagonal.
    - If a permutation is valid during diagonal check, add it to our result.

Time complexity: O(N!N) - N! for checking all permutations and O(N) for checking if permutation is valid 
Space complexity: O(N) 
"""
# Check if the cell (wanted col, wanted rol) is safe to place a new queen 
def is_safe(board, wanted_row, wanted_col):

    for i in range(len(board)):
        placed_col = i + 1
        placed_row = board[i]

        # Check if the wanted place is on the same diagonal with placed queens
        if abs(placed_col - wanted_col) == abs(placed_row - wanted_row):
            return False
    
    return True 

def naive_nqueen_util(col, N, board, results, visited_rows):
    if col > N:
        results.append(board.copy())
        return 
    
    for row in range(1, N + 1):
        if not visited_rows[row]:                # If the row was not visited
            if is_safe(board, row, col):    # Check if safe to place a queen at current row, col
                visited_rows[row] = True         # Mark row was visited
                board.append(row)           # Place a queen at current row, col
                # Go to the next collumn 
                naive_nqueen_util(col + 1, N, board, results, visited_rows)

                # Once getting a solution, backtrack to find another solution 
                board.pop()                 
                visited_rows[row] = False


def naive_nqueen(N):
    results = []            # store all solutions 
    visited_rows = [False] * (N + 1)    # record rows visited
    board = []              # board[i] records the row where the queen at column i is placed

    naive_nqueen_util(1, N, board, results, visited_rows)  # Start placing queen on the col 1
    
    return results


"""
2. Pruning approach by using three arrays recording rows, diagonals visited to avoid checking is the cell is safe to place a queen 

- Time complexity O(N!)
- Space complexity O(N)
"""

def prunning_nqueen_util(col, N, board, results, visited_rows, visited_diag1, visited_diag2):
    if col > N:
        results.append(board.copy())
        return
    
    for row in range(1, N + 1):
        if not visited_rows[row] and not visited_diag1[row + col] and not visited_diag2[row - col + N]:
            visited_rows[row] = True
            visited_diag1[row + col] = True
            visited_diag2[row - col + N] = True
            board.append(row)

            prunning_nqueen_util(col + 1, N, board, results, visited_rows, visited_diag1, visited_diag2)

            # Backtrack
            visited_rows[row] = False
            visited_diag1[row + col] = False
            visited_diag2[row - col + N] = False
            board.pop()


def prunning_nqueen(N):
    results = []
    board = []
    visited_rows = [False] * (N + 1)
    visited_diag1 = [False] * (2*N + 1)
    visited_diag2 = [False] * (2*N + 1)

    prunning_nqueen_util(1, N, board, results, visited_rows, visited_diag1, visited_diag2)

    return results


'''
3. Prunning backtracking with bitmasks
'''
def is_safe(row, col, rows, diag1, diag2):
    return not((rows >> row) & 1) and \
        not((diag1 >> (row + col)) & 1) and \
        not((diag2 >> (row - col + N)) & 1)


def bitmasks_nqueen_util(col, N, board, results, rows, diag1, diag2):
    if col > N:
        results.append(board.copy())
        return 
    
    for row in range(1, N + 1):
        if is_safe(row, col, rows, diag1, diag2):
            rows |= (1 << row)
            diag1 |= (1 << (row + col))
            diag2 |= (1 << (row - col + N))
            board.append(row)

            bitmasks_nqueen_util(col + 1, N, board, results, rows, diag1, diag2)

            # Backtracking
            rows &= ~(1 << row)
            diag1 &= ~(1 << (row + col))
            diag2 &= ~(1 << (row - col + N))
            board.pop()

def bitmasks_nqueen(N):
    results = []
    board = []

    bitmasks_nqueen_util(1, N, board, results, 0, 0, 0)

    return results
    
def solve_nqueen(N):
    #return naive_nqueen(N)
    #return prunning_nqueen(N)
    return bitmasks_nqueen(N)

if __name__ == '__main__':
    N = 4
    
    results = solve_nqueen(N)

    for sol in results:
        print(sol)

    print("Number of solutions is: ", len(results))