import json 
from player_state_class import Player_State
from game_state_class import Game_State

# planets_file = open('planets.json')
# planets_dict = json.load(planets_file)

# developments_file = open('developments.json')
# developments_dict = json.load(developments_file)

#print(developments_dict)

def create_starting_players(game_state):
    players = []
    for player in range(1, game_state.amount_of_players + 1):
        players.append(Player_State(f"player_{player}", 1, 0, 0, [], [], [], 0, [], []))
    game_state.players = players

def create_starting_game_state(amount_of_players):
    current_game_state = Game_State(amount_of_players)
    create_starting_players(current_game_state)
    print(current_game_state)
    current_game_state.print_players()

create_starting_game_state(3)


