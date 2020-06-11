class Character():
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def hit(self, char):
        char.health -= (self.attack - self.defense)


class Knight(Character):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.health = 150
        self.defense = 20
        self.attack = 25


class Warrior(Character):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.health = 100
        self.defense = 5
        self.attack = 40

    def potion(self, char):
        char.health += 35
        return "35"


class Healer(Character):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.health = 75
        self.defense = 0
        self.attack = 20

    def heal(self, char):
        char.health += 75


class Enemy(Character):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.health = 150
        self.defense = 20
        self.attack = 30


