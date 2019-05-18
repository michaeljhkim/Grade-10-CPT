class Stats:
    def __init__(self, health, armour, inventory, state):
        self.name = input()
        self.health = health
        self.armour = armour
        self.inventory = inventory
        self.state = state

    def print_name(self, damage):
        print(self.health - damage)


telling = Stats(100, 100, "A lot of stuff", "healthy")
telling.print_name(10)










