
import random

WINNING_BOARD_CONFIGURATIONS = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
COMP_SYMBOL = "X"
HUMAN_SYMBOL = "O"

def board_print(board_list):
    print("-------------")
    print("| " + board_list[0] + " | " + board_list[1] + " | " + board_list[2] + " |")
    print("-------------")
    print("| " + board_list[3] + " | " + board_list[4] + " | " + board_list[5] + " |")
    print("-------------")
    print("| " + board_list[6] + " | " + board_list[7] + " | " + board_list[8] + " |")
    print("-------------")


def check_winner(board_list):
    for combo in WINNING_BOARD_CONFIGURATIONS:
        combo_square1 = combo[0]
        combo_square2 = combo[1]
        combo_square3 = combo[2]
        if board_list[combo_square1] == board_list[combo_square2] == board_list[combo_square3] != " ":
            return True
    return False


def best_move_for_player(outcomes, current_symbol):
    opponent_symbol = get_other_symbol(current_symbol)

    if current_symbol in outcomes:
        return current_symbol
    elif "T" in outcomes:
        return "T"
    else:
        return opponent_symbol


def get_other_symbol(symbol):
    if symbol == "X":
        return "O"
    else:
        return "X"

def get_available_squares(board):
    available_squares = []
    for i, symbol in enumerate(board):
        if symbol == " ":
            available_squares.append(i)
    return available_squares


def get_comp_move(board_list):
    game_results = {}

    available_squares = get_available_squares(board_list)
    for square in available_squares:
        board_list[square] = COMP_SYMBOL
        game_results[square] = get_game_outcomes(board_list, HUMAN_SYMBOL)

    for square, result in game_results.items():
        if result == COMP_SYMBOL:
            return square
    for square, result in game_results.items():
        if result == "T":
            return square
    for square, result in game_results.items():
        if result == HUMAN_SYMBOL:
            return square

    return square


def get_game_outcomes(board_list, symbol_turn):
    # board_print(board_list)
    available_squares = get_available_squares(board_list)

    # if there are no spots left it is a tie
    if len(available_squares) == 0:
        return "T"

    # Otherwise see what the results in the remaining game tree
    else:
        # store the result, given the player choses a move that's optimal for their end of game each turn
        game_outcomes = []
        for square in available_squares:
            # place a symbol
            board_list[square] = symbol_turn

            # check for a winner
            game_won = check_winner(board_list)
            if game_won:
                #if the game is won stop recursing, the current symbol has won and is both the min and max outcome for this subgame
                game_outcomes.append(symbol_turn)

            else:
                # recurse and record results for subgames
                next_symbol = get_other_symbol(symbol_turn)
                sub_game_outcomes = get_game_outcomes(board_list, next_symbol)
                # print(game_outcomes, sub_game_outcomes)
                game_outcomes.append(sub_game_outcomes)

            board_list[square] = " "

    # Find the best course of action that the current player would take
    return best_move_for_player(game_outcomes, symbol_turn)



# Starting the game
board_list = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
print("Are you ready to play tic tac toe?")
board_print(board_list)

symbol = "O"
game_over = False
available_squares = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
turn_count = 0
while not game_over:
    turn_count = turn_count + 1
    # symboling the board
    print("It's " + symbol + "'s turn!")

    if symbol == "O":
        chosen_square = input("Where do you want to play? ")
    else:
        square = get_comp_move(board_list)

    while chosen_square not in available_squares:
        print("That square is not available! Please try again.")
        print("The available squares are:", available_squares)
        chosen_square = input("Where do you want to play? ")

    available_squares.remove(chosen_square)
    square_index = int(chosen_square) - 1
    board_list[square_index] = symbol

    board_print(board_list)

    # Checking the winner
    game_won = check_winner(board_list)
    if game_won:
        print("The winner is " + symbol + " !")
        game_over = True
    elif turn_count == 9:
        print("It's a tie!")
        game_over = True

    # Taking turns
    if symbol == "O":
        symbol = "X"
    elif symbol == "X":
        symbol = "O"
