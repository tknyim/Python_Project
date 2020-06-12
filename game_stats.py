class Character():
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def hit(self, char):
        char.health -= (self.attack - self.defense)

    def potion(self):
        amount = 30
        self.health += amount
        return amount


class Knight(Character):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.health = 200
        self.defense = 5
        self.attack = 25


class Warrior(Character):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.health = 120
        self.defense = 5
        self.attack = 40


class Gremlin(Character):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.health = 100
        self.defense = 5
        self.attack = 8

class Werewolf(Character):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.health = 150
        self.defense = 10
        self.attack = 10

class Chimera(Character):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.health = 200
        self.defense = 15
        self.attack = 12

class Bahamut(Character):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.health = 300
        self.defense = 20
        self.attack = 15

