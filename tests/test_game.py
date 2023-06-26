from lib.game import Game
from unittest.mock import Mock

"""
Initialises with a length and width of 10
"""
def test_initialises_with_a_length_and_width_of_10():
    game = Game()
    assert game.rows == 10
    assert game.cols == 10

"""
Initialises with five ships of length 2, 3, 3, 4, 5
"""
def test_initialises_with_five_ships_of_right_length():
    game = Game()
    unplaced_ships = game.unplaced_ships()
    assert len(unplaced_ships) == 5
    assert unplaced_ships[0].length == 2
    assert unplaced_ships[1].length == 3
    assert unplaced_ships[2].length == 3
    assert unplaced_ships[3].length == 4
    assert unplaced_ships[4].length == 5

"""
Initialises with a totally empty board
"""
def test_initialises_with_a_totally_empty_board():
    game = Game()
    for row in range(1, 11):
        for col in range(1, 11):
            assert not game.ship_at(row, col)

"""
When we place a ship
Then its place on the board is marked out
"""
def test_when_we_place_a_ship_then_its_place_on_the_board_is_marked_out():
    game = Game()
    game.place_ship(length=2, orientation="vertical", row=3, col=2)
    assert game.ship_at(3, 2)
    assert game.ship_at(4, 2)
    assert not game.ship_at(3, 3)
    assert not game.ship_at(4, 3)
    assert not game.ship_at(3, 1)
    assert not game.ship_at(4, 1)

"""
When a ship is placed, unplaced_ships removes ship
"""
def test_place_ship_removes_ship_from_unplaced_ships():
    game = Game()
    mock_ships = [Mock(length=2), Mock(length=3), Mock(length=3), Mock(length=4), Mock(length=5)]
    game.ships_unplaced = mock_ships
    game.place_ship(length=2, orientation="vertical", row=3, col=2)
    result = game.unplaced_ships()
    '''mocks are never identical so cannot set like this:
    assert result == [Mock(length=3), Mock(length=3), Mock(length=4), Mock(length=5)]'''
    for ship in result:
        assert ship.length != 2

"""
When a ship is placed, adds object to ships_placed
"""
def test_place_ship_adds_ships_to_placed_ships():
    game = Game()
    game.place_ship(length=5, orientation="vertical", row=3, col=2)
    assert len(game.ships_placed) == 1
    ship_placement = game.ships_placed[0]
    assert ship_placement.length == 5
    assert ship_placement.orientation == "vertical"
    assert ship_placement.row == 3
    assert ship_placement.col == 2