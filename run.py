import sys
from lib.game import Game
from lib.user_interface import UserInterface
from lib.user import User


class TerminalIO:
    def readline(self):
        return sys.stdin.readline()

    def write(self, message):
        sys.stdout.write(message)

io = TerminalIO()

'''
    As a player
    So that I can play against a human opponent
    I would like to play a two-player game
'''
    
game_1 = Game()
game_2 = Game()
player_1 = User(game_1, None, "Claudia")
player_2 = User(game_2, None, "Tim")
user_interface_1 = UserInterface(io, game_1, player_1)
user_interface_2 = UserInterface(io, game_2, player_2)

game_over = False
player_one_setup = False
player_two_setup = False

player_1.opponent = player_2
player_2.opponent = player_1

current_player = player_1

#set up player one board:
user_interface_1.run(player_1)
while player_one_setup == False:
    user_interface_1.next_run(player_1)
    if len(game_1.ships_unplaced) < 1:
        print(f"Player one:\n{player_1.board}")
        player_one_setup = True
        break

#set up player two board
user_interface_2.run(player_2)
while player_two_setup == False:
    user_interface_2.next_run(player_2)
    if len(game_2.ships_unplaced) < 1:
        player_two_setup = True

print(f"Player one:\n{player_1.board}\nPlayer two:\n{player_2.board}")

while not game_over:

    current_player.shoot()
    
    if current_player.is_game_over() == True:
        game_over = True
        print(f"{current_player} wins!")
    else:
        if current_player == player_1:
            current_player = player_2
        else:
            current_player = player_1
    


