import json 
from player_state_class import Player_State
from game_state_class import Game_State
from planet_class import Planet
from development_class import Development

# planets_file = open('planets.json')
# planets_dict = json.load(planets_file)

def load_developments(game_state):
    developments = []
    developments_file = open('developments.json')
    developments_dict = json.load(developments_file)
    for development in developments_dict:
        d = Development(development['name'], development['cost'])
        developments.append(d)
    game_state.development_bag = developments

def load_planets(game_state):
    planets = []
    planets_file = open('planets.json')
    planets_dict = json.load(planets_file)
    for planet in planets_dict:
        p = Planet(planet['name'], planet['cost'], planet['credit_gain'], planet['remove_dice'], planet['gained_dice_color'], planet['gained_dice_type'] )
        planets.append(p)
    game_state.planet_bag = planets

def create_starting_players(game_state):
    players = []
    for player in range(1, game_state.amount_of_players + 1):
        players.append(Player_State(f"player_{player}", 1, 0, 0, [], [], [], 0, [], []))
    game_state.players = players

def create_starting_game_state(amount_of_players):
    current_game_state = Game_State(amount_of_players)
    create_starting_players(current_game_state)
    load_developments(current_game_state)
    load_planets(current_game_state)
    print(current_game_state)
    current_game_state.print_players()
    #current_game_state.print_development_bag()
    current_game_state.print_planet_bag()

create_starting_game_state(3)