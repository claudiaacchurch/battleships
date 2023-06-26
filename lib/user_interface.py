class UserInterface:
    def __init__(self, io, game, player):
        self.io = io
        self.game = game
        self.player = player

    def run(self, player):
        self._show(f"Welcome to the game {player.name}!")
        self._show("Set up your ships first.")
        self._show(self._format_board(player)) # show board first
        self._show("You have these ships remaining: {}".format(
            self._ships_unplaced_message()))
        self._prompt_for_ship_placement()
        self._show("This is your board now:")
        self._show(self._format_board(player))

    def next_run(self, player):
        self._show("You have these ships remaining: {}".format(
            self._ships_unplaced_message()))
        self._prompt_for_ship_placement()
        self._show("This is your board now:")
        self._show(self._format_board(player))
        
    def _show(self, message):
        self.io.write(message + "\n")

    def _prompt(self, message):
        self.io.write(message + "\n")
        return self.io.readline().strip()

    def _ships_unplaced_message(self):
        ship_lengths = [str(ship.length) for ship in self.game.unplaced_ships()]
        return ", ".join(ship_lengths)

    '''
        As a player
        So that I can have a coherent game
        I would like ships to be constrained not to overlap
    '''

    def check_no_overlap(self, orientation, row, col, length):
        for i in range(int(length)): # loop iterates over ship length (0, 1, 2)
            if orientation == "vertical":
                if self.game.ship_at(int(row) + i, int(col)): # increment by i to check span of rows, col for 'v' is constant
                    return False
            else:
                if self.game.ship_at(int(row), int(col) + i):
                    return False
        return True

    def _prompt_for_ship_placement(self):

        # outer loop that check_if_placement_valid and check_no_overlap continue to
        while True:

            while True:
                ship_length = self._prompt("Which do you wish to place?")
                lengths = self._ships_unplaced_message()
                split_lengths = [x.strip() for x in lengths.split(',')]
                try:
                    ship_length = int(ship_length)
                    if str(ship_length) in split_lengths:
                        break
                    else:
                        self._show("Ship does not exist.")
                except ValueError:
                    self._show("Ship length needs to be int.")
                    continue
    
            while True:
                ship_orientation = self._prompt("Vertical or horizontal? [vh]")
                if type(ship_orientation) != str or ship_orientation not in "vh":
                    self._show("Please choose 'v' or 'h'")
                    continue
                else:
                    break

            ''' 
                As a player
                So that I can have a coherent game
                I would like ships to be constrained to be on the board 
            '''

            while True:
                ship_row = self._prompt("Which row?")
                try:
                    if int(ship_row) < 1 or int(ship_row) > 10:
                        self._show("Row not in range of board, please choose again.")
                        continue #continue the loop if row is not valid
                    else:
                        break #when input is valid break the loop and continue to next requirement
                except ValueError:
                    self._show("Row need to be int")
                    continue 
   
            while True:
                ship_col = self._prompt("Which column?")
                try:
                    if int(ship_col) < 1 or int(ship_col) > 10:
                        self._show("Col not in range of board, please choose again.")
                        continue
                    else:
                        break
                except ValueError:
                    self._show("Col needs to be int")
                    continue 
            
            if self.check_no_overlap(ship_orientation, ship_row, ship_col, ship_length) == False:
                self._show("Ship overlaps with another ship.")
                continue
            else:
                self.game.place_ship(
                    length=int(ship_length),
                    orientation={"v": "vertical", "h": "horizontal"}[ship_orientation],
                    row=int(ship_row),
                    col=int(ship_col),
                )
                break #outer loop A


    def _format_board(self, player):
        rows = []
        for row in range(1, self.game.rows + 1):
            row_cells = []
            for col in range(1, self.game.cols + 1):
                if self.game.ship_at(row, col):
                    row_cells.append("S")
                else:
                    row_cells.append(".")
            rows.append("".join(row_cells))
        player.board = "\n".join(rows)
        return "\n".join(rows)


        


