# Kim Apted is testing the intermediate work book

def print_board(board):
    print("-------------")
    print("| {} | {} | {} |".format(board[0], board[1], board[2]))
    print("-------------")
    print("| {} | {} | {} |".format(board[3], board[4], board[5]))
    print("-------------")
    print("| {} | {} | {} |".format(board[6], board[7], board[8]))
    print("-------------")

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
print_board(board)

symbol = "O"
print("It's {}'s turn!".format(symbol))

square = input("Which square do you want to choose? ")
square_index = int(square)

board[square_index] = symbol
print_board(board)

if symbol == "O":
    symbol = "X"
elif symbol == "X":
    symbol = "O"
