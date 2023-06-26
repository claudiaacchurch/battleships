from lib.user import User
from unittest.mock import Mock, patch
from lib.user_interface import UserInterface
from tests.terminal_interface_helper_mock import TerminalInterfaceHelperMock

"""
User.shoot adds shot to self.shots
"""
def test_user_shoot_adds_to_shots():
    with patch('builtins.input', side_effect=[3,2]) as mock_input:
        game1 =Mock()
        game2 = Mock()
        user1 = User(game1, None, "Tim")
        user2 = User(game2, user1, "Claudia")
        user2.shoot()
        print(user2.shots)
        assert user2.shots == [(2, 1)]
        assert user2.shots != [(3, 2)]
                           

"""
User.opponent.board returns the board for opponent
"""
def test_user_gets_opponents_board():
    game1 =Mock()
    game2 = Mock()
    user1 = User(game1, None, "Tim")
    user1.board = ("\n".join([
            "..........",
            "..........",
            ".S........",
            ".S........",
            "....SSS...",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
        ]))
    user2 = User(game2, user1, "Claudia")
    result = user2.opponent.board
    assert result == ("\n".join([
            "..........",
            "..........",
            ".S........",
            ".S........",
            "....SSS...",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
        ]))



"""
User.shoot returns user.opponents_board with hit
"""

def test_user_shoots_hit_opponent_board():
    with patch('builtins.input', side_effect=[3,2]) as mock_input:
        game1 =Mock()
        game2 = Mock()
        user1 = User(game1, None, "Tim")
        user1.board = ("\n".join([
                "..........",
                "..........",
                ".S........",
                ".S........",
                "....SSS...",
                "..........",
                "..........",
                "..........",
                "..........",
                ".........."
            ]))
        user2 = User(game2, user1, "Claudia")
        user2.shoot()
        result = user2.opponents_board
        print(user2.shots)
        assert result == ("\n".join([
                "..........",
                "..........",
                ".✅........",
                "..........",
                "..........",
                "..........",
                "..........",
                "..........",
                "..........",
                ".........."
            ]))


"""
User.shoot returns user.opponents_board with miss
"""
def test_user_shoots_hit_opponent_board():
    with patch('builtins.input', side_effect=[3,2]) as mock_input:
        game1 =Mock()
        game2 = Mock()
        user1 = User(game1, None, "Tim")
        user1.board = ("\n".join([
                "..........",
                "..........",
                ".S........",
                ".S........",
                "....SSS...",
                "..........",
                "..........",
                "..........",
                "..........",
                ".........."
            ]))
        user2 = User(game2, user1, "Claudia")
        user2.shoot()
        result = user2.opponents_board
        print(user2.shots)
        assert result == ("\n".join([
                "..........",
                "..........",
                ".✅........",
                "..........",
                "..........",
                "..........",
                "..........",
                "..........",
                "..........",
                ".........."
            ]))

"""
User.shoot returns error message when sho already fired
"""
def test_user_shoots_miss_opponent_board():
    with patch('builtins.input', side_effect=[5,2]) as mock_input:
        game1 =Mock()
        game2 = Mock()
        user1 = User(game1, None, "Tim")
        #mock referenced functions
        game1.ship_at.return_value = False
        user2 = User(game2, user1, "Claudia")
        user2.shoot()
        #print(f'\n{user1.board}')
        result = user2.opponents_board
        assert result == ("\n".join([
                "..........",
                "..........",
                "..........",
                "..........",
                ".❌........",
                "..........",
                "..........",
                "..........",
                "..........",
                ".........."
            ]))

"""
User.is_game_over returns True when all opponents ships are sunk
"""
def test_game_over_when_all_ships_sunk():
    game1 =Mock()
    game2 = Mock()
    user1 = User(game1, None, "Tim")
    user2 = User(game2, user1, "Claudia")
    ship_placement_1 = Mock()
    ship_placement_2 = Mock()
    game1.ships_placed = [ship_placement_1, ship_placement_2]
    ship_placement_1.is_sunk = True
    ship_placement_2.is_sunk = True
    result = user2.is_game_over()
    assert result == True