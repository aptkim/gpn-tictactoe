# Kim Apted is testing the intermediate work book

import random

comp_symbol = "X"
human_symbol = "O"

winning_combos = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]]

def get_other_symbol(symbol):
    if symbol == comp_symbol:
        return human_symbol
    else:
        return comp_symbol

def get_available_squares(board):
    available_squares = []
    for i, symbol in enumerate(board):
        if symbol == " ":
            available_squares.append(i)
    return available_squares

def get_comp_move(board):
    available_squares = get_available_squares(board)
    return random.choice(available_squares)

def check_winner(board):
    for combo in winning_combos:
        symbol_0 = board[combo[0]]
        symbol_1 = board[combo[1]]
        symbol_2 = board[combo[2]]

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

while not game_over:
    print("It's {}'s turn!".format(symbol))

    if symbol == human_symbol:
        square = input("Which square do you want to choose? ")
        square_index = int(square)
    else:
        square_index = get_comp_move(board)

    board[square_index] = symbol
    print_board(board)
    
    game_over = check_winner(board)
    if game_over:
        print("Game over! The winner is", symbol)

    symbol = get_other_symbol(symbol)
