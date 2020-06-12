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
        self.defense = 10
        self.attack = 30


class Warrior(Character):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.health = 150
        self.defense = 5
        self.attack = 350


class Gremlin(Character):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.health = 40
        self.defense = 0
        self.attack = 20

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

