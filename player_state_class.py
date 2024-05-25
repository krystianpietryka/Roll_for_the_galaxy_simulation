class Player_State:
    def __init__(self, name, credits, victory_points, tile_amount, dice_in_citizenry, dice_in_cup, all_dice, tiles_played, planet_stack, development_stack):
        self.name = name
        self.credits = credits
        self.victory_points = victory_points
        self.tile_amount = tile_amount
        self.dice_in_citizenry = dice_in_citizenry
        self.dice_in_cup = dice_in_cup
        self.all_dice = all_dice
        self.tiles_played = tiles_played
        self.planet_stack = planet_stack
        self.development_stack = development_stack

    def __repr__(self):
        planet_names = ", ".join(planet.name for planet in self.planet_stack)
        development_names = ", ".join(development.name for development in self.development_stack)
        return f"{self.name} State:\n| Credits: {self.credits}\n| Victory_Points: {self.victory_points}\n| Tiles Played: {self.tiles_played}\n| Dice in cup: {self.dice_in_cup}\n| Dice in Citizenry: {self.dice_in_citizenry}\n| Planet Stack: {planet_names}\n| Development Stack: {development_names}\n"