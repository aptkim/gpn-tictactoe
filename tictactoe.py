#Beginners Better Version

def print_grid(grid_list):
    print("-------------")
    print("| " + grid_list[0] + " | " + grid_list[1] + " | " + grid_list[2] + " |")
    print("-------------")
    print("| " + grid_list[3] + " | " + grid_list[4] + " | " + grid_list[5] + " |")
    print("-------------")
    print("| " + grid_list[6] + " | " + grid_list[7] + " | " + grid_list[8] + " |")
    print("-------------")

def check_for_winner(grid_list):
    if (grid_list[0] == grid_list[1] and grid_list[1] == grid_list[2]
        or grid_list[3] == grid_list[4] and grid_list[4] == grid_list[5]
        or grid_list[6] == grid_list[7] and grid_list[7] == grid_list[8]
        or grid_list[0] == grid_list[3] and grid_list[3] == grid_list[6]
        or grid_list[1] == grid_list[4] and grid_list[4] == grid_list[7]
        or grid_list[2] == grid_list[5] and grid_list[5] == grid_list[8]
        or grid_list[0] == grid_list[4] and grid_list[4] == grid_list[8]
        or grid_list[2] == grid_list[4] and grid_list[4] == grid_list[6]):
        return True
    else:
        return False

def check_move_for_win(grid_list, square, symbol):
    grid_copy = list(grid_list)
    grid_copy[int(square) - 1] = symbol
    return check_for_winner(grid_copy)

# Exercsie 2.1 (Storing players' names)
player0 = input("Who will be naughts? ")
print("The computer will be crosses!")
print("Let's play tic tac toe " + player0 + " vs the computer!")

# Task 3.1 & 3.2 (Storing the game)
grid_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
available_squares = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Task 4.1 (Smarter printer)
print_grid(grid_list)

# Task 5.1 & 5.2 (First turn)
current_player = player0
current_symbol = "0"

# Task 7.1 (Counting turns)
turns = 0
# Task 8.1 (Watching for a winner)
game_won = False

# Task 7.2 & 8.2
while turns < 9 and game_won == False:
    # Task 5.3 (Ask what square they want to take)
    if current_player == player0:
        print(current_player + " it's your turn!")
        print("The available squares are:")
        print(available_squares)
        input_square = input("Which square would you like? ")

        #Validating the input square
        while input_square not in available_squares:
            print("Square " + input_square + " is not one of the available squares! Please try again.")
            print("It's still " + current_player + "'s turn.")
            input_square = input("what square would you like out of " + ", ".join(available_squares) + " ?\n")
    else:
        input_square = available_squares[0]
        for square in available_squares:
            if check_move_for_win(grid_list, square, current_symbol):
                input_square = square
        print("The computer player has chosen square " + input_square)

    # Task 5.4 (Update available squares)
    available_squares.remove(input_square)
    # Task 5.7 (Update the game board)
    grid_list[int(input_square) - 1] = current_symbol
    # Task 5.8 (Print the grid again)
    print_grid(grid_list)

    # 8.4 & 8.5 (Check for the winner - function)
    game_won = check_for_winner(grid_list)
    
    # Task 9.1 (Defining the winner)
    if game_won == True:
        winning_player = current_player

    # Task 6.1 (Changing turns - defaults to Player0)
    if current_player == player0:
        current_player = "computer"
        current_symbol = "X"
    else:
        current_player = player0
        current_symbol = "0"

    # Task 7.3
    turns = turns + 1

# Task 9.2 (Annoucing the results)
if game_won == True:
    if winning_player == player0:
        print("Congratulations!")
        print(winning_player + ", you won!")
    else:
        print("You've been beaten by the computer!")
else:
    print("GAME OVER!")
    print("It's a draw!")