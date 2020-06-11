class Character():
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def hit(self, char):
        char.health -= self.attack

    def move(self, dir):
        if dir == "left":
            self.position["x"] -= self.speed
        elif dir == "right":
            self.position["x"] += self.speed
        elif dir == "up":
            self.position["y"] -= self.speed
        elif dir == "down":
            self.position["y"] += self.speed


class Knight(Character):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.health = 200
        self.speed = 10
        self.defense = 50
        self.attack = 20 


class Warrior(Character):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.health = 150
        self.speed = 14
        self.defense = 20
        self.attack = 40

    def potion(self, char):
        char.health += 50
        return "50"


class Healer(Character):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.health = 100
        self.speed = 12
        self.defense = 10
        self.attack = 20

    def heal(self, char):
        char.health += 200


class Enemy(Character):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.health = 130
        self.speed = 10
        self.defense = 20
        self.attack = 30


