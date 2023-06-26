class User():
    def __init__(self, game, opponent, name):
        self.board = ""
        self.opponent = opponent
        self.opponents_board = "\n".join([
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
        ])
        self.game = game
        self.shots = []
        self.name = name

    def shoot(self):
        while True:
            try:
                ship_row = int(input(f"{self.name} choose a row:")) - 1
                ship_col = int(input("Choose a column:")) - 1
            except ValueError:
                print("Input must be an integer. Try again.")
                continue
            except IndexError:
                print("Row and column numbers must be between 1 and 10. Try again.")

            # avoid duplicates
            if (ship_row, ship_col) not in self.shots:
                self.shots.append((ship_row, ship_col))
                rows = self.opponents_board.split("\n")
                if self.opponent.game.ship_at(ship_row+1, ship_col+1):
                    print("HIT!")
                    ship = self.opponent.game.which_ship(ship_row+1, ship_col+1)
                    ship.hit()
                    rows[ship_row] = rows[ship_row][:ship_col] + "✅" + rows[ship_row][ship_col + 1:]
                else:
                    print("MISS!")
                    rows[ship_row] = rows[ship_row][:ship_col] + "❌" + rows[ship_row][ship_col + 1:]
                self.opponents_board = "\n".join(rows)
                print(self.opponents_board)
                break
            else:
                print("This shot has already been fired.")
    

    def is_game_over(self):
        return all(ship.is_sunk for ship in self.opponent.game.ships_placed)



        
    
