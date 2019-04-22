# Kim Apted is testing the advanced work book

winning_combos = [[0, 1, 2], 
                  [3, 4, 5], 
                  [6, 7, 8],
                  [0, 3, 6], 
                  [1, 4, 7], 
                  [2, 5, 8],
                  [0, 4, 8],
                  [2, 4, 6]]

def check_winner(board):
    for combo in winning_combos:
        combo_part_0 = combo[0]
        combo_part_1 = combo[1]
        combo_part_2 = combo[2]
        symbol_0 = board[combo_part_0]
        symbol_1 = board[combo_part_1]
        symbol_2 = board[combo_part_2]

        if symbol_0 == symbol_1 == symbol_2 and symbol_0 != " ":
            return True

    return False

def print_board(board):
    print("-------------")
    print("| {} | {} | {} |".format(board[0], board[1], board[2]))
    print("-------------")
    print("| {} | {} | {} |".format(board[3], board[4], board[5]))
    print("-------------")
    print("| {} | {} | {} |".format(board[6], board[7], board[8]))
    print("-------------")

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
game_over = False

symbol = "O"
counter = 0

while not game_over:
    print("It's {}'s turn!".format(symbol))

    square = input("Which square do you want to choose? ")
    square_index = int(square)

    board[square_index] = symbol
    print_board(board)
    counter += 1
    
    game_over = check_winner(board)
    if game_over:
        print("Game over! The winner is", symbol)
        
    if counter == 9:
        print("Game over! It's a tie!")
        break
    
    if symbol == "O":
        symbol = "X"
    elif symbol == "X":
        symbol = "O"
