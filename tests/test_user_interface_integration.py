import unittest
from lib.user_interface import UserInterface
from lib.game import Game
from lib.user import User
from tests.terminal_interface_helper_mock import TerminalInterfaceHelperMock
import pytest

class TestUserInterface(unittest.TestCase):
    def test_ship_setup_scenario(self):
        io = TerminalInterfaceHelperMock()
        game1 = Game()
        user1 = User(game1, None, "Claudia")
        interface = UserInterface(io, game1, user1)
        
        io.expect_print("Welcome to the game Claudia!")
        io.expect_print("Set up your ships first.")
        io.expect_print("\n".join([
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
        ]))
        io.expect_print("You have these ships remaining: 2, 3, 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("2")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("3")
        io.expect_print("Which column?")
        io.provide("2")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".S........",
            ".S........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
        ]))
        interface.run(user1)
        

    """
    If placement of ship's row not within the board raise error
    """
    def test_ship_setup_scenario_row_error(self):
        io = TerminalInterfaceHelperMock()
        game1 = Game()
        user1 = User(game1, None, "Claudia")
        interface = UserInterface(io, game1, user1)
        io.expect_print("Welcome to the game Claudia!")
        io.expect_print("Set up your ships first.")
        io.expect_print("\n".join([
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
        ]))
        io.expect_print("You have these ships remaining: 2, 3, 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("2")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("12")
        io.expect_print("Row not in range of board, please choose again.")
        io.expect_print("Which row?")
        io.provide("3")
        io.expect_print("Which column?")
        io.provide("2")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".S........",
            ".S........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
        ]))
        interface.run(user1)

    """
    If placement of ship's col not within the board print error
    """
    def test_ship_setup_scenario_col_error(self):
        io = TerminalInterfaceHelperMock()
        game1 = Game()
        user1 = User(game1, None, "Claudia")
        interface = UserInterface(io, game1, user1)
        io.expect_print("Welcome to the game Claudia!")
        io.expect_print("Set up your ships first.")
        io.expect_print("\n".join([
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
        ]))
        io.expect_print("You have these ships remaining: 2, 3, 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("2")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide('3')
        io.expect_print("Which column?")
        io.provide('11')
        io.expect_print("Col not in range of board, please choose again.")
        io.expect_print("Which column?")
        io.provide('2')
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".S........",
            ".S........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
        ]))
        interface.run(user1)

    """
    If placement of ship overlaps with another ship raise error
    """
    def test_ship_setup_scenario_overlap_error(self):
            io = TerminalInterfaceHelperMock()
            game1 = Game()
            user1 = User(game1, None, "Claudia")
            interface = UserInterface(io, game1, user1)
            io.expect_print("Welcome to the game Claudia!")
            io.expect_print("Set up your ships first.")
            io.expect_print("\n".join([
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
            ]))
            io.expect_print("You have these ships remaining: 2, 3, 3, 4, 5")
            io.expect_print("Which do you wish to place?")
            io.provide("2")
            io.expect_print("Vertical or horizontal? [vh]")
            io.provide("v")
            io.expect_print("Which row?")
            io.provide('3')
            io.expect_print("Which column?")
            io.provide('2')
            io.expect_print("This is your board now:")
            io.expect_print("\n".join([
            "..........",
            "..........",
            ".S........",
            ".S........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
            ]))
            interface.run(user1)
            io.expect_print("You have these ships remaining: 3, 3, 4, 5")
            io.expect_print("Which do you wish to place?")
            io.provide("3")
            io.expect_print("Vertical or horizontal? [vh]")
            io.provide("v")
            io.expect_print("Which row?")
            io.provide('3')
            io.expect_print("Which column?")
            io.provide('2')
            io.expect_print("Ship overlaps with another ship.")

            io.expect_print("Which do you wish to place?")
            io.provide("3")
            io.expect_print("Vertical or horizontal? [vh]")
            io.provide("v")
            io.expect_print("Which row?")
            io.provide('6')
            io.expect_print("Which column?")
            io.provide('2')
            io.expect_print("This is your board now:")
            io.expect_print("\n".join([
            "..........",
            "..........",
            ".S........",
            ".S........",
            "..........",
            ".S........",
            ".S........",
            ".S........",
            "..........",
            ".........."
            ]))
            interface.next_run(user1)
    
    """
    If orientation not str raise error
    """
    def test_if_horizontal_vertical_is_string(self):
        io = TerminalInterfaceHelperMock()
        game1 = Game()
        user1 = User(game1, None, "Claudia")
        interface = UserInterface(io, game1, user1)
        io.expect_print("Welcome to the game Claudia!")
        io.expect_print("Set up your ships first.")
        io.expect_print("\n".join([
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
        ]))
        io.expect_print("You have these ships remaining: 2, 3, 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("2")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("5")
        io.expect_print("Please choose 'v' or 'h'")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide('6')
        io.expect_print("Which column?")
        io.provide('2')
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
        "..........",
        "..........",
        "..........",
        "..........",
        "..........",
        ".S........",
        ".S........",
        "..........",
        "..........",
        ".........."
        ]))
        interface.run(user1)
    
    """
    If length is not int raise error
    """

    def test_if_length_is_int(self):
        io = TerminalInterfaceHelperMock()
        game1 = Game()
        user1 = User(game1, None, "Claudia")
        interface = UserInterface(io, game1, user1)
        io.expect_print("Welcome to the game Claudia!")
        io.expect_print("Set up your ships first.")
        io.expect_print("\n".join([
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
        ]))
        io.expect_print("You have these ships remaining: 2, 3, 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("v")
        io.expect_print("Ship length needs to be int.")
        io.expect_print("Which do you wish to place?")
        io.provide("2")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide('3')
        io.expect_print("Which column?")
        io.provide('11')
        io.expect_print("Col not in range of board, please choose again.")
        io.expect_print("Which column?")
        io.provide('2')
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".S........",
            ".S........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
        ]))
        interface.run(user1)
    
    """
    If int not in unplaced_ships raise error
    """
    def test_if_length_is_available(self):
        io = TerminalInterfaceHelperMock()
        game1 = Game()
        user1 = User(game1, None, "Claudia")
        interface = UserInterface(io, game1, user1)
        io.expect_print("Welcome to the game Claudia!")
        io.expect_print("Set up your ships first.")
        io.expect_print("\n".join([
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
        ]))
        io.expect_print("You have these ships remaining: 2, 3, 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("2")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("3")
        io.expect_print("Which column?")
        io.provide("2")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".S........",
            ".S........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
        ]))
        interface.run(user1)
        io.expect_print("You have these ships remaining: 3, 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("2")
        io.expect_print("Ship does not exist.")
        io.expect_print("Which do you wish to place?")
        io.provide("3")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide('6')
        io.expect_print("Which column?")
        io.provide('2')
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
        "..........",
        "..........",
        ".S........",
        ".S........",
        "..........",
        ".S........",
        ".S........",
        ".S........",
        "..........",
        ".........."
        ]))
        interface.next_run(user1)

"""
If row is not int raise error
"""
def test_ship_setup_scenario_row_error_string():
        io = TerminalInterfaceHelperMock()
        game1 = Game()
        user1 = User(game1, None, "Claudia")
        interface = UserInterface(io, game1, user1)
        io.expect_print("Welcome to the game Claudia!")
        io.expect_print("Set up your ships first.")
        io.expect_print("\n".join([
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
        ]))
        io.expect_print("You have these ships remaining: 2, 3, 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("2")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("f")
        io.expect_print("Row need to be int")
        io.expect_print("Which row?")
        io.provide("3")
        io.expect_print("Which column?")
        io.provide("2")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".S........",
            ".S........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
        ]))
        interface.run(user1)

"""
If col is not int raise error
"""
def test_ship_setup_scenario_col_error_string():
        io = TerminalInterfaceHelperMock()
        game1 = Game()
        user1 = User(game1, None, "Claudia")
        interface = UserInterface(io, game1, user1)
        io.expect_print("Welcome to the game Claudia!")
        io.expect_print("Set up your ships first.")
        io.expect_print("\n".join([
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
        ]))
        io.expect_print("You have these ships remaining: 2, 3, 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("2")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("3")
        io.expect_print("Which column?")
        io.provide("g")
        io.expect_print("Col needs to be int")
        io.expect_print("Which column?")
        io.provide("2")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".S........",
            ".S........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
        ]))
        interface.run(user1)
