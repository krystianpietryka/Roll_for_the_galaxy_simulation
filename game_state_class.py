class Game_State:
    def __init__(self, amount_of_players):
        self.amount_of_players = amount_of_players
        self.game_end = 0
        self.victory_points_left = amount_of_players * 12
        self.players = []

    def __repr__(self):
        return f"Victory Points Left: {self.victory_points_left}, Is game ended? {self.game_end} "
    
    def print_players(self):
        for p in self.players:
            print(p)