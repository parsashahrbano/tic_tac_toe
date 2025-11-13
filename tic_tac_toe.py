def print_board(board):
    #creating page
    print("  1 2 3")
    print("__________")
    for i, row in enumerate(board,start=1):
        print(f"{i}|"+"|".join(row)+"|")
        print("__________")

def check_winner(board,current_player):
    #who is winner ?!
    #check row and column
    for i in range(3):
        if all(board[i][j]==current_player for j in range(3)):
            return True
        if all(board[j][i]==current_player for j in range(3)):
            return True
    # check diameter
    if all(board[i][i]==current_player for i in range(3)):
        return True
    if all(board[i][2-i]==current_player for i in range(3)):
        return True
    return False 

def is_draw(board,current_player):
    # is it draw ?!
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    #main function
    board=[[" " for _ in range(3)]for _ in range(3)]
    current_player="X"
    print("game on!")
    print_board(board)
    while True:
        print (f"\n {current_player} it's your turn")
        try:
            row=int(input("(1-3) write down your row_number: "))-1
            col=int(input("(1-3) write down your column_number: "))-1
        except ValueError:
            print("please write an integer number between 1-3")
            continue
        if row not in range(3) or col not in range(3):
            print(" The number you wrote is out of range")
            continue
        if board[row][col] != " ":
            print("This cell is occupied")
            continue
        #Take action
        board[row][col]=current_player
        print_board(board)

        #check_winner
        if check_winner(board,current_player):
            print(f"{current_player} you win")
            break
        #is_draw
        if is_draw(board,current_player):
            print("It's over")
            break
        #switch among players
        current_player="O"if current_player=="X" else "X"

if __name__=="__main__":
    tic_tac_toe()