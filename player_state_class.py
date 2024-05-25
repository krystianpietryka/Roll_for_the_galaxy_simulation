class Player_State:
    def __init__(self, name, credits, victory_points, tile_amount, dice_in_population, dice_in_cup, all_dice, tiles_played, planets_stack, developments_stack):
        self.name = name
        self.credits = credits
        self.victory_points = victory_points
        self.tile_amount = tile_amount
        self.dice_in_population = dice_in_population
        self.dice_in_cup = dice_in_cup
        self.all_dice = all_dice
        self.tiles_played = tiles_played
        self.planets_stack = planets_stack
        self.developments_stack = developments_stack
    def __repr__(self):
        return f"Player {self.name}: Credits: {self.credits}, Victory_Points: {self.victory_points}, Tiles Played: {self.tiles_played}, Dice in cup: {self.dice_in_cup}, Dice in Population: {self.dice_in_population}, Planet Stack: {self.planets_stack}, Development Stack: {self.developments_stack}"