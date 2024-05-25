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
    faction_planets_file = open('faction_planets.json')
    faction_planets_dict = json.load(faction_planets_file)
    faction_developments_file = open('faction_developments.json')
    faction_developments_dict = json.load(faction_developments_file)
    for tile in faction_tiles_dict:
        faction_tiles.append(tile)
    for player in game_state.players:
        current_player_planet_stack = copy.deepcopy(player.planet_stack)
        current_player_development_stack = copy.deepcopy(player.development_stack)
        random_faction_tile = random.choice(faction_tiles)
        random_faction_tile_planets = random_faction_tile.get("planet")
        # random_faction_tile_planets_data = faction_developments_dict.get
        # print(random_faction_tile_planets)
        # print(isinstance(random_faction_tile_planets, list))
        random_faction_tile_developments = random_faction_tile.get("development")
        if random_faction_tile_planets:
                if isinstance(random_faction_tile_planets, list):
                     for p in random_faction_tile_planets:
                          faction_planets_desired_dict = next((item for item in faction_planets_dict if item['name'] == p), None)
                          current_planet_object = Planet(faction_planets_desired_dict["name"], faction_planets_desired_dict["cost"], faction_planets_desired_dict["credit_gain"], faction_planets_desired_dict["remove_dice"], faction_planets_desired_dict["gained_dice_color"], faction_planets_desired_dict["gained_dice_type"])
                          current_player_planet_stack.append(current_planet_object)
                else:
                    faction_planets_desired_dict = next((item for item in faction_planets_dict if item['name'] == random_faction_tile_planets), None)
                    current_planet_object = Planet(faction_planets_desired_dict["name"], faction_planets_desired_dict["cost"], faction_planets_desired_dict["credit_gain"], faction_planets_desired_dict["remove_dice"], faction_planets_desired_dict["gained_dice_color"], faction_planets_desired_dict["gained_dice_type"])    
                    current_player_planet_stack.append(current_planet_object)
        if random_faction_tile_developments:
                if isinstance(random_faction_tile_developments, list):
                     for d in random_faction_tile_developments:
                          faction_developments_desired_dict = next((item for item in faction_developments_dict if item['name'] == d), None)
                          current_development_object = Development(faction_developments_desired_dict["name"], faction_developments_desired_dict["cost"])   
                          current_player_development_stack.append(current_development_object)
                else:
                    faction_developments_desired_dict = next((item for item in faction_developments_dict if item['name'] == random_faction_tile_developments), None)
                    current_development_object = Development(faction_developments_desired_dict["name"], faction_developments_desired_dict["cost"])   
                    current_player_development_stack.append(current_development_object)
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
        current_player_planet_stack.append(random_home_world_planet)
        player.planet_stack = current_player_planet_stack
        planets.remove(random_home_world_planet)

def create_starting_players(game_state):
    players = []
    for player in range(1, game_state.amount_of_players + 1):
        players.append(Player_State(f"player_{player}", 1, 0, 0, [], [], [], 0, [], []))
    game_state.players = players

def distribute_starting_white_dice(game_state):
     players = game_state.players
     for player in players:
          current_dice_in_citizenry = player.dice_in_citizenry
          current_dice_in_cup = player.dice_in_cup
          current_dice_in_citizenry.append(["white", "white"])
          current_dice_in_cup.append(["white", "white", "white"])
          player.dice_in_citizenry = current_dice_in_citizenry
          player.dice_in_cup = current_dice_in_cup

# def populate_planet(game_state, player_state, planet, planet_source):
#      if
     

def create_starting_game_state(amount_of_players):
    current_game_state = Game_State(amount_of_players)
    create_starting_players(current_game_state)
    load_bag_developments(current_game_state)
    load_bag_planets(current_game_state)
    print(current_game_state)
    distribute_home_world_planets_to_players(current_game_state)
    distribute_faction_tiles_to_players(current_game_state)
    distribute_starting_white_dice(current_game_state)
    current_game_state.print_players()
    #current_game_state.print_development_bag()
    #current_game_state.print_planet_bag()

create_starting_game_state(3)