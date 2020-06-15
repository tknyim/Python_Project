class Character():
    def __init__(self, name, position):
        self.name = name
        self.position = position



class Knight(Character):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.health = 225
        self.defense = 5
        self.attack = 30
        self.pot = 10

class Warrior(Character):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.health = 150
        self.defense = 5
        self.attack = 40
        self.pot = 10


class Gremlin(Character):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.health = 40
        self.defense = 5
        self.attack = 25
        self.score = 30

class Werewolf(Character):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.health = 150
        self.defense = 10
        self.attack = 10
        self.score = 25

class Chimera(Character):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.health = 200
        self.defense = 15
        self.attack = 12
        self.score = 50

class Bahamut(Character):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.health = 300
        self.defense = 20
        self.attack = 15
        self.score = 200


class H(Character):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.health = 9999
        self.defense = 0
        self.attack = 200
        self.pot = 0
