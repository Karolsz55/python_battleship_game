from random import randint

scores = {"computer": 0, "player": 0}

class Battleship:
    def __init__(self, board_size=5, num_ships=3, ship_size=3):
        # Initialize the game parameters
        self.board_size = board_size
        self.num_ships = num_ships
        self.ship_size = ship_size
        self.board = [['O' for x in range(self.board_size)] for y in range(self.board_size)]
        self.ships_placed = 0
        self.num_turns = 0