class Development:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def __repr__(self):
        return f"Development {self.name}: Cost: {self.cost} "
    