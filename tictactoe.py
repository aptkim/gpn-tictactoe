#Beginners Better Version
# Exercsie 2.1 (Storing players' names)
player0 = input("Who will be naughts? ")
print("The computer will be crosses!")
print("Let's play tic tac toe " + player0 + " vs the computer!")

# Task 3.1 & 3.2 (Storing the game)
grid_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
available_squares = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Task 4.1 (Smarter printer)
print("-------------")
print("| " + grid_list[0] + " | " + grid_list[1] + " | " + grid_list[2] + " |")
print("-------------")
print("| " + grid_list[3] + " | " + grid_list[4] + " | " + grid_list[5] + " |")
print("-------------")
print("| " + grid_list[6] + " | " + grid_list[7] + " | " + grid_list[8] + " |")
print("-------------")

# Task 5.1 & 5.2 (First turn)
current_player = player0
current_symbol = "0"

# Task 7.1 (Counting turns)
turns = 0
# Task 8.1 (Watching for a winner)
game_won = "no"

# Task 7.2 & 8.2
while turns < 9 and game_won == "no":
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
        print("The computer player has chosen square " + input_square)

    # Task 5.4 (Update available squares)
    available_squares.remove(input_square)
    # Task 5.5 (Convert to number)
    input_square_int = int(input_square)
    # Task 5.6 (Find the location for the symbol)
    grid_list_item = input_square_int - 1
    # Task 5.7 (Update the game board)
    grid_list[grid_list_item] = current_symbol

    # Task 5.8 (Print the grid again)
    print("-------------")
    print("| " + grid_list[0] + " | " + grid_list[1] + " | " + grid_list[2] + " |")
    print("-------------")
    print("| " + grid_list[3] + " | " + grid_list[4] + " | " + grid_list[5] + " |")
    print("-------------")
    print("| " + grid_list[6] + " | " + grid_list[7] + " | " + grid_list[8] + " |")
    print("-------------")

    # 8.4 & 8.5 (Check for the winner - if statements)
    if (grid_list[0] == grid_list[1] and grid_list[1] == grid_list[2]
        or grid_list[3] == grid_list[4] and grid_list[4] == grid_list[5]
        or grid_list[6] == grid_list[7] and grid_list[7] == grid_list[8]
        or grid_list[0] == grid_list[3] and grid_list[3] == grid_list[6]
        or grid_list[1] == grid_list[4] and grid_list[4] == grid_list[7]
        or grid_list[2] == grid_list[5] and grid_list[5] == grid_list[8]
        or grid_list[0] == grid_list[4] and grid_list[4] == grid_list[8]
        or grid_list[2] == grid_list[4] and grid_list[4] == grid_list[6]):

        game_won = "yes"
        # Task 9.1 (Defining the winner)
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
if game_won == "yes":
    if winning_player == player0:
        print("Congratulations!")
        print(winning_player + ", you won!")
    else:
        print("You've been beaten by the computer!")
else:
    print("GAME OVER!")
    print("It's a draw!")