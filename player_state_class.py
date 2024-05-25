class Player_State:
    def __init__(self, name, credits, victory_points, tile_amount, dice_in_population, dice_in_cup, all_dice, tiles_played, planet_stack, development_stack):
        self.name = name
        self.credits = credits
        self.victory_points = victory_points
        self.tile_amount = tile_amount
        self.dice_in_population = dice_in_population
        self.dice_in_cup = dice_in_cup
        self.all_dice = all_dice
        self.tiles_played = tiles_played
        self.planet_stack = planet_stack
        self.development_stack = development_stack
    def __repr__(self):
        return f"{self.name}: Credits: {self.credits}, Victory_Points: {self.victory_points}, Tiles Played: {self.tiles_played}, Dice in cup: {self.dice_in_cup}, Dice in Population: {self.dice_in_population}, Planet Stack: {self.planet_stack}, Development Stack: {self.development_stack}"