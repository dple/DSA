def is_valid_tictactoe(mat):
    win = 0
    no_x = 0
    no_o = 0
    rows, cols = len(mat), len(mat[0])

    for i in range(rows):
        if mat[i] == ['X', 'X', 'X'] or mat[i] == ['O', 'O', 'O']:
            win += 1
        for j in range(cols):
            if mat[i][j] == 'X':
                no_x += 1
            if mat[i][j] == 'O':
                no_o += 1
    if no_o >= 6 or no_x >= 6 or no_o > no_x + 1 or no_x > no_o + 1:
        return False
    
    for i in range(cols):
        no_o, no_x = 0, 0
        for j in range(rows):
            if mat[j][i] == 'X':
                no_x += 1
            else:
                no_o += 1
        if no_o == 3 or no_x == 3:
            win += 1
    
    if win >= 2:
        return False
    
    return True

    
    

if __name__ == '__main__':
    ttt = [
        ['X', 'X', 'O'], 
        ['O', 'O', 'X'],
        ['X', ' ', ' ']
    ]

    print(is_valid_tictactoe(ttt))