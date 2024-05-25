import json 
import copy
import random
from player_state_class import Player_State
from game_state_class import Game_State
from planet_class import Planet
from development_class import Development

#add faction developments
#implement development actions


# planets_file = open('planets.json')
# planets_dict = json.load(planets_file)

def load_bag_developments(game_state):
    developments = []
    developments_file = open('developments.json')
    developments_dict = json.load(developments_file)
    for development in developments_dict:
        d = Development(development['name'], development['cost'])
        developments.append(d)
    game_state.development_bag = developments

def load_bag_planets(game_state):
    planets = []
    planets_file = open('planets.json')
    planets_dict = json.load(planets_file)
    for planet in planets_dict:
        p = Planet(planet['name'], planet['cost'], planet['credit_gain'], planet['remove_dice'], planet['gained_dice_color'], planet['gained_dice_type'] )
        planets.append(p)
    game_state.planet_bag = planets

def distribute_faction_tiles_to_players(game_state):
    faction_tiles = []
    faction_tiles_file = open('faction_tiles.json')
    faction_tiles_dict = json.load(faction_tiles_file)
    for tile in faction_tiles_dict:
        faction_tiles.append(tile)
    for player in game_state.players:
        current_player_planet_stack = copy.deepcopy(player.planet_stack)
        current_player_development_stack = copy.deepcopy(player.development_stack)
        random_faction_tile = random.choice(faction_tiles)
        random_faction_tile_planets = random_faction_tile.get("planet")
        # print(random_faction_tile_planets)
        # print(isinstance(random_faction_tile_planets, list))
        random_faction_tile_developments = random_faction_tile.get("development")
        if random_faction_tile_planets:
                if isinstance(random_faction_tile_planets, list):
                     for p in random_faction_tile_planets:
                          current_player_planet_stack.append(p)
                else:
                    current_player_planet_stack.append(random_faction_tile_planets)
        if random_faction_tile_developments:
                if isinstance(random_faction_tile_developments, list):
                     for d in random_faction_tile_developments:
                          current_player_development_stack.append(d)
                else:
                    current_player_development_stack.append(random_faction_tile_developments)
        player.planet_stack = current_player_planet_stack
        player.development_stack = current_player_development_stack
        faction_tiles.remove(random_faction_tile)

def distribute_home_world_planets_to_players(game_state):
    planets = []
    planets_file = open('home_world_planets.json')
    planets_dict = json.load(planets_file)
    for planet in planets_dict:
        p = Planet(planet['name'], planet['cost'], planet['credit_gain'], planet['remove_dice'], planet['gained_dice_color'], planet['gained_dice_type'] )
        planets.append(p)
    for player in game_state.players:
        current_player_planet_stack = copy.deepcopy(player.planet_stack)
        random_home_world_planet = random.choice(planets)
        current_player_planet_stack.append(random_home_world_planet.name)
        player.planet_stack = current_player_planet_stack
        planets.remove(random_home_world_planet)

def create_starting_players(game_state):
    players = []
    for player in range(1, game_state.amount_of_players + 1):
        players.append(Player_State(f"player_{player}", 1, 0, 0, [], [], [], 0, [], []))
    game_state.players = players

def create_starting_game_state(amount_of_players):
    current_game_state = Game_State(amount_of_players)
    create_starting_players(current_game_state)
    load_bag_developments(current_game_state)
    load_bag_planets(current_game_state)
    print(current_game_state)
    distribute_home_world_planets_to_players(current_game_state)
    distribute_faction_tiles_to_players(current_game_state)
    current_game_state.print_players()
    #current_game_state.print_development_bag()
    #current_game_state.print_planet_bag()

create_starting_game_state(3)