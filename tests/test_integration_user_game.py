from lib.user import User
from lib.game import Game
import unittest
from unittest.mock import patch

"""
User can enter shots from command line
"""

class TestUser(unittest.TestCase): # mock input function that accepts user input from cmnd line
    @patch('builtins.input', side_effects=[1, 1]) # where patch mocks the inputs in order 1, 1
    def test_user_can_enter_shots_from_command_line(self, mock_input):
        game1 = Game()
        game2 = Game()
        user1 = User(game1, None, "Claudia")
        user2 = User(game2, None, "Tim")
        user1.opponent = user2
        user2.opponent = user1
        user1.shoot()
        self.assertEqual(user1.shots, [(0, 0)]) #checks if a == b in (a, b)
        #user.shots will be 0 indexing from ship_placement
    

"""
User.shoot() responds with hit and appends opponents board
"""

class TestUserHit(unittest.TestCase):
    @patch('builtins.input', side_effect=[1, 2])
    def test_user_shoot_appends_opponents_board(self, mock_input):
        game1 = Game()
        game2 = Game()
        user1 = User(game1, None, "Claudia")
        user2 = User(game2, None, "Tim")
        user1.opponent = user2
        user2.opponent = user1
        game2.place_ship(length=3, orientation='horizontal', row=1, col=2) # ship placement uses 0 indexing
        user1.shoot()
        result = user1.opponents_board
        expected_board = "\n".join([
            ".✅........",
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
        assert result  == expected_board

"""
User.shoot() responds with miss and appends opponents board
"""

class TestUserMiss(unittest.TestCase):
    @patch('builtins.input', side_effect=[1, 2])
    def test_user_shoot_appends_opponents_board_with_miss(self, mock_input):
        game1 = Game()
        game2 = Game()
        user1 = User(game1, None, "Claudia")
        user2 = User(game2, None, "Tim")
        user1.opponent = user2
        user2.opponent = user1
        game2.place_ship(length=3, orientation='horizontal', row=5, col=2) # ship placement uses 0 indexing
        user1.shoot()
        result = user1.opponents_board
        expected_board = "\n".join([
            ".❌........",
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
        assert result  == expected_board

"""
User.shoot raises error if col not int
"""

class TestUserColError(unittest.TestCase):
    @patch('builtins.input', side_effect=[1, "fg"])
    def test_user_shoot_invalid_col(self, mock_input):
        game1 = Game()
        game2 = Game()
        user1 = User(game1, None, "Claudia")
        user2 = User(game2, None, "Tim")
        user1.opponent = user2
        user2.opponent = user1
        game2.place_ship(length=3, orientation='horizontal', row=5, col=2) # ship placement uses 0 indexing
        user1.shoot()
        result = user1.opponents_board
        assert result  == "Input must be an integer. Try again."




"""
User.shoot raises error if row not int
"""
"""
User.shoot returns error message when sho already fired
"""

"""
User.is_game_over is True when all ships ares sunk
"""