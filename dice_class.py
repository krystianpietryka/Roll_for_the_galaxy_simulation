class Dice:
    def __init__(self, type, color, side_1, side_2, side_3, side_4, side_5, side_6):
        self.type = type
        self.color = color
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
        self.side_4 = side_4
        self.side_5 = side_5
        self.side_6 = side_6

    def __repr__(self):
        return f"{self.type} ({self.color}) Dice Sides:\n| {self.side_1}\n|  {self.side_2}\n|  {self.side_3}\n|  {self.side_4}\n|  {self.side_5}\n|  {self.side_6}\n"