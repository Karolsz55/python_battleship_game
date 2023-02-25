import random


class Battleship:
    """
    Main game board class, sets number and size of ships, board size
    player name
    Has methods for printing the board adding ships and guesses
    """
    def __init__(self, board_size=5, num_ships=3, ship_size=3):
        # Method for initializing the game parameters
        self.board_size = board_size
        self.num_ships = num_ships
        self.ship_size = ship_size
        self.board = [['O' for x in range(self.board_size)] for y in range(self.board_size)]
        self.ships_placed = 0
        self.num_turns = 0
        self.player_name = ""

    def place_ships(self):
        # Method for randomly placing the ships on the board
        while self.ships_placed < self.num_ships:
            ship_row = random.randint(0, self.board_size-1)
            ship_col = random.randint(0, self.board_size-1)
            if self.board[ship_row][ship_col] == 'O':
                self.board[ship_row][ship_col] = 'S'
                self.ships_placed += 1

    def print_board(self):
        # Methpd for printing the game board
        for row in self.board:
            print(" ".join(row))

    def get_player_name(self):
        # Method for getting the player's name
        self.player_name = input("What is your name? ")

    def play_game(self):
        # Method for playing the game
        print("Welcome to Battleship, {}!".format(self.player_name))
        print("Let's play!")
        self.print_board()
        while True:
            guess_row, guess_col = self.get_guess()
            result = self.check_guess(guess_row, guess_col)
            self.num_turns += 1
            if result == 'win':
                print("Congratulations, {}! You won in {} turns!".format(self.player_name, self.num_turns))
                self.print_board()
                break
            elif result == 'hit':
                print("Congratulations, {}! You hit my battleship!".format(self.player_name))
            elif result == 'miss':
                print("Sorry, {}! You missed my battleship!".format(self.player_name))
            self.computer_turn()
    
    def get_guess(self):
        # Method for getting the user's guess and validating it
        while True:
            try:
                guess_row = int(input("Guess Row (0-{}): ".format(self.board_size-1)))
                guess_col = int(input("Guess Col (0-{}): ".format(self.board_size-1)))
                if not (0 <= guess_row < self.board_size and 0 <= guess_col < self.board_size):
                    raise ValueError
                if self.board[guess_row][guess_col] == 'X':
                    print("You already guessed that one. Try again.")
                    continue
                return guess_row, guess_col
            except ValueError:
                print("Invalid input. Please enter a number between 0 and {}.".format(self.board_size-1))

    def check_guess(self, guess_row, guess_col):
        # Method for checking the user's guess and returning the result
        if self.board[guess_row][guess_col] == 'S':
            self.board[guess_row][guess_col] = 'X'
            if self.check_win():
                return 'win'
            return 'hit'
        elif self.board[guess_row][guess_col] == 'X':
            return 'repeat'
        else:
            self.board[guess_row][guess_col] = 'X'
            return 'miss'
    
    def check_win(self):
        # Method for checking if the game has been won
        for row in self.board:
            if 'S' in row:
                return False
        return True
    
    def computer_turn(self):
        # Let the computer take a turn
        while True:
            comp_guess_row = random.randint(0, self.board_size-1)
            comp_guess_col = random.randint(0, self.board_size-1)
            if self.board[comp_guess_row][comp_guess_col] == 'X':
                continue
            elif self.board[comp_guess_row][comp_guess_col] == 'S':
                print("The computer sank one of your battleships!")
                self.board[comp_guess_row][comp_guess_col] = 'X'
                if self.check_win():
                    print("Sorry, the computer won!")
                    self.print_board()
                    exit()
                break
            else:
                print("The computer missed!")
                self.board[comp_guess_row][comp_guess_col] = 'X'
                break
        self.print_board()