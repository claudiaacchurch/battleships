from lib.ship import Ship
from lib.ship_placement import ShipPlacement


class Game:
    def __init__(self, rows=10, cols=10):
        self.ships_placed = []
        self.ships_unplaced = [Ship(2), Ship(3), Ship(3), Ship(4), Ship(5)]
        self.rows = rows
        self.cols = cols

    def unplaced_ships(self):
        # switched to have unplaced_ships in init so I can remove 
        return self.ships_unplaced

    def place_ship(self, length, orientation, row, col):
        ship_placement = ShipPlacement(
            length=length,
            orientation=orientation,
            row=row,
            col=col,
        )
        # remove placed ship from ships to place
        for ship in self.ships_unplaced:
            if ship.length == ship_placement.length:
                self.ships_unplaced.remove(ship) 
        self.ships_placed.append(ship_placement)

    def ship_at(self, row, col):
        for ship_placement in self.ships_placed:
            if ship_placement.covers(row, col):
                return True
        return False
    
    def which_ship(self, row, col):
        for ship_placement in self.ships_placed:
            if ship_placement.covers(row, col):
                return ship_placement
        return None

    


