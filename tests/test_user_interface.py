from tests.terminal_interface_helper_mock import TerminalInterfaceHelperMock
from lib.user_interface import UserInterface
from unittest.mock import Mock

"""
Test ship set up empty board
"""
def test_user_interface_set_up():
    user1 = Mock()
    io = TerminalInterfaceHelperMock()
    game1 = Mock()
    interface = UserInterface(io, game1, user1)
    game1.rows = 10
    game1.cols = 10
    game1.ship_at.return_value = False
    user1.board = "\n".join([
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
    assert interface._format_board(user1) == user1.board
