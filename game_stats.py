class Character():
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def hit(self, char):
        char.health -= (self.attack - self.defense)


class Knight(Character):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.health = 200
        self.defense = 5
        self.attack = 25

    def potion(self, char):
        char.health += 25
        return "25"


class Warrior(Character):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.health = 120
        self.defense = 5
        self.attack = 40

    def potion(self, char):
        char.health += 30
        return "30"


class Healer(Character):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.health = 100
        self.defense = 5
        self.attack = 15

    def heal(self, char):
        char.health += 40
        return "40"


class Mob(Character):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.health = 100
        self.defense = 5
        self.attack = 8

class Enemy(Character):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.health = 150
        self.defense = 10
        self.attack = 10

class Semi_Boss(Character):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.health = 200
        self.defense = 15
        self.attack = 12

class Boss(Character):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.health = 300
        self.defense = 20
        self.attack = 15

