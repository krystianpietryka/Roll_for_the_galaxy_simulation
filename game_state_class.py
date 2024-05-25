class Game_State:
    def __init__(self, amount_of_players):
        self.amount_of_players = amount_of_players
        self.game_end = 0
        self.victory_points_left = amount_of_players * 12
        self.players = []
        self.planet_bag = []
        self.development_bag = []

    def __repr__(self):
        return f"Game State:\n| Victory Points Left: {self.victory_points_left}\n| Planets Left: {len(self.planet_bag)}\n| Developments Left: {len(self.development_bag)}\n"
    
    def print_players(self):
        for p in self.players:
            print(p)

    def print_development_bag(self):
        for d in self.development_bag:
            print(d)

    def print_planet_bag(self):
        for p in self.planet_bag:
            print(p)