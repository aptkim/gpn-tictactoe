WINNING_BOARD_CONFIGURATIONS = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


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
            return board_list[combo_square1]
    return None


def evaluate_board(board_list):
    winner = check_winner(board_list)
    
    if winner == "X":
        # Computer won
        return 1
    elif winner == "O":
        # Human won
        return -1
    
    if " " not in board_list:
        # Game tied
        return 0
    
    # There's still moves... How do we score that!?
    return 0


def choose_computer_move(board_list, available_squares): 
    best_move = available_squares[0]
    best_outcome = -1
    
    for square in available_squares:
        board_list[int(square) - 1] = "X"
        outcome = evaluate_board(board_list)
        board_list[int(square) - 1] = " "
        
        if outcome > best_outcome:
            best_move = square
            best_outcome = outcome
    
    return best_move


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
        # Human players turn
        chosen_square = input("Where do you want to play? ")

        while chosen_square not in available_squares:
            print("That square is not available! Please try again.")
            print("The available squares are:", available_squares)
            chosen_square = input("Where do you want to play? ")
    else:
        # Computer players turn
        chosen_square = choose_computer_move(board_list, available_squares)

    available_squares.remove(chosen_square)
    square_index = int(chosen_square) - 1
    board_list[square_index] = symbol

    board_print(board_list)
    print("Computer's evaluation of the current board:", evaluate_board(board_list))

    # Checking the winner
    game_won = check_winner(board_list)
    if game_won:
        print("The winner is " + game_won + " !")
        game_over = True
    elif turn_count == 9:
        print("It's a tie!")
        game_over = True

    # Taking turns
    if symbol == "O":
        symbol = "X"
    elif symbol == "X":
        symbol = "O"


