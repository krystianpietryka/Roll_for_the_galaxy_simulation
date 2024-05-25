class Planet:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def __repr__(self):
        return f"Planet {self.name}: Cost: {self.cost} "
    