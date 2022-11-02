board = [['O', 'X', 'X'],
         ['X', 'X', 'O'],
         ['O', 'X', 'X']]

row_len = len(board)
col_len = len(board[0])
found_winner = False

for i in range(row_len):
    if board[i][0] == board[i][1] == board[i][2]:
        found_winner = True
        print(f"{board[i][0]} is the winner!")
        
for i in range(col_len):
    if board[0][i] == board[1][i] == board[2][i]:
        found_winner = True
        print(f"{board[0][i]} is the winner!")
        
if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
    found_winner = True
    print(f"{board[0][0]} is the winner!")
    
if board[0][2] == board[1][1] and board[0][2] == board[2][0]:
    found_winner = True
    print(f"{board[0][2]} is the winner!")

if not found_winner:
    print("this is a tie.")