import random


scores = {"computer": 0, "player": 0}

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
