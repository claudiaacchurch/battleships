class ShipPlacement:
    def __init__(self, length, orientation, row, col):
        self.length = length
        self.orientation = orientation
        self.row = row
        self.col = col
        self.hits = 0
        self.is_sunk = False

    def covers(self, row, col):
        if self.orientation == "vertical":
            if self.col != col:
                return False
            return self.row <= row < self.row + self.length
        else:
            if self.row != row:
                return False
            return self.col <= col < self.col + self.length

    def hit(self):
        self.hits += 1
        if self.hits == self.length:
            print("sunk ship!")
            self.is_sunk = True

    def __repr__(self):
        return f"ShipPlacement(length={self.length}, orientation={self.orientation}, row={self.row}, col={self.col})"


