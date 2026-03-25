def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def change(player):
    if player == "X":
        return "O"
    else:
        return "X"
    
        
def check_winner(board):
    lines = [
        [0,1,2], [3,4,5], [6,7,8],  # sorok
        [0,3,6], [1,4,7], [2,5,8],  # oszlopok
        [0,4,8], [2,4,6]            # átlók 
    ]

    for line in lines:
        if board[line[0]] == board[line[1]] and board[line[1]] == board[line[2]]:
          if board[line[0]] not in ["1","2","3","4","5","6","7","8","9"]:
                return board[line[0]]  # "X" vagy "O"

    return None


def main():
    board = ["1","2","3","4","5","6","7","8","9"]
    player = "X"
    

    while True:
        
        print_board(board)
        winner = check_winner(board)
        if winner:  
            print(f"{winner} nyert!")
            break
        
        if not any(elem != "X" and elem != "O" for elem in board):
            print("It's a draw")
            break

        
        try:
            choice = int(input("Choose a number between 1-9: "))
            if board[choice - 1] not in ["X", "O"] and 1 <= choice <= 9:
                board[choice - 1] = player
            else:
                print("This cell is already used")
                continue
        except (ValueError, IndexError):
            print("Only 1 - 9")
            continue
    
        player = change(player)

if __name__ == '__main__':
    main()
