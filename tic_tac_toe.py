# Kim Apted is testing the intermediate work book

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

symbol = "O"

square = input("Which square do you want to choose? ")
square_index = int(square)

board[square_index] = symbol

print("-------------")
print("| {} | {} | {} |".format(board[0], board[1], board[2]))
print("-------------")
print("| {} | {} | {} |".format(board[3], board[4], board[5]))
print("-------------")
print("| {} | {} | {} |".format(board[6], board[7], board[8]))
print("-------------")
