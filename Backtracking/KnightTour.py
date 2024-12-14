"""
Implement knight tour problem using backtracking 
- Time complexity: O(8^(N^2))
- Space complexity: O(N^2)
"""
N = 8

def is_safe(x, y, board):
    if (x >= 0 and y >= 0 and x < N and y < N and board[x][y] == -1):
        return True
    return False

def knight_util(N, board, curr_x, curr_y, move_x, move_y, moves):
    if (moves == N**2):
        return True 
    
    for i in range(8):      # 8 possible moves of knight from one position
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if is_safe(new_x, new_y, board):
            board[new_x][new_y] = moves

            if knight_util(N, board, new_x, new_y, move_x, move_y, moves + 1):
                return True 
            
            # Backtracking 
            board[new_x][new_y] = -1

    return False 

def knight(N):    
    board = [[-1 for _ in range(N)] for _ in range(N)]    
    # 8 potential moves of a knight from one position 
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]   
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    board[0][0] = 0                      # Tour is initialized the the corner 
    moves = 1                               # Number of moves 

    if (not knight_util(N, board, 0, 0, move_x, move_y, moves)):
        print("No solution exist!")
    
    else:
        for row in board:
            print(*row)
            

    


if __name__ == '__main__':
    
    knight(N)
