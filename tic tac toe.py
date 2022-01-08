def take_input(player):    
    global x
    global y
    player_number = {"o":1, "x":2}
    print(f"Enter x, y coordinates for player {player_number[player]}({player}):")
    x=int(input("x="))-1
    y=int(input("y="))-1
    player_move(board,player)

def createboard():
    board=[
            [" "," "," "],
            [" "," "," "],
            [" "," "," "]
            ]
    return board


def printboard(board):
    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
    print("--+---+--")
    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("--+---+--")
    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
    print("\n")




def player_move(board,player):
    cordinates=[0,1,2]
    if x in cordinates and y in cordinates:
        if board[x][y] != " ":
            print('Coordinates not empty')
            take_input(player)
        else:
            board[x][y]=player
    else:
        print("Invalid move.")
        take_input(player)
        
        
        
        
def check_winner(board,player):
    if board[0][0]==player and board[0][1]==player and board[0][2]==player:
        return player;
    if board[1][0]==player and board[1][1]==player and board[1][2]==player:
        return player;
    if board[2][0]==player and board[2][1]==player and board[2][2]==player:
        return player;
    
    if board[0][0]==player and board[1][0]==player and board[2][0]==player:
        return player;
    if board[0][1]==player and board[1][1]==player and board[2][1]==player:
        return player;
    if board[0][2]==player and board[1][2]==player and board[2][2]==player:
        return player;
    
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        return player;
    if board[0][2]==player and board[1][1]==player and board[2][0]==player:
        return player;
        
    if board[0][0]!=" " and board[0][1]!=" " and board[0][2]!=" " and board[1][0]!=" " and board[1][1]!=" " and board[1][2]!=" " and board[2][0]!=" " and board[2][1]!=" " and board[2][2]!=" ":
        return "draw";
  
    
    
#coding
board= createboard()
printboard(board)
player="o"
winner=None    

while winner==None:
    take_input(player)
    printboard(board)
    winner=check_winner(board,player)
    if player=="o":
        player="x"
    else:
        player="o"

winner=winner.lower()        
if winner=="o":
    print(f"Player 1 wins!!!")
elif winner=="x":
    print(f"Player 2 wins!!!")
elif winner=="draw":
    print(f"It's a draw.")