class Planet:
    def __init__(self, name, cost, credit_gain, remove_dice, gained_dice_color, gained_dice_type):
        self.name = name
        self.cost = cost
        self.credit_gain = credit_gain
        self.remove_dice = remove_dice
        self.gained_dice_color = gained_dice_color
        self.gained_dice_type = gained_dice_type

    def __repr__(self):
        parts = [f"Planet {self.name}: Cost: {self.cost}"]

        if self.credit_gain != 0:
            parts.append(f"Credit Gain: {self.credit_gain}")

        if self.remove_dice:
            parts.append(f"Dice Removed: {len(self.remove_dice)}")

        if self.gained_dice_color and self.gained_dice_type:
            gained_dice = "/".join(
                f"{color.capitalize()} {'into' if type == 'cup' else 'as'} {type.capitalize()}" 
                for color, type in zip(self.gained_dice_color, self.gained_dice_type)
            )
            parts.append(f"Gained Dice: {gained_dice}")

        return " | ".join(parts)