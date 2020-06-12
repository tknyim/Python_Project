import map_size
import movement
import encounter
import random
from game_stats import Knight, Warrior, Bahamut



game_board = map_size.gen_board(6,6)
print(game_board)
nextStep = False

player = input("What is your name? ")
position = map_size.starting_position(map_size)
boss = Bahamut("Boss",position[1])

while nextStep == False:
    print("\nChoose a character: [ 1. Warrior   2. Dark Knight ]")
    select = int(input(">> "))
    if select == 1:
        player = Warrior(player,position[0])
        print("\n Warrior Selected")
        nextStep = True

    elif select == 2:
        player = Knight(player, position[0])
        print("\n Knight Selected")
        nextStep = True
    else:
        print("\nNot a character.")


gameplay = True
win = False
battle = False
direction = True


while gameplay:
    print("Your position is x: %s , y: %s \n" % (player.position.x, player.position.y))
    print("Your distance between the boss is %s \n" % map_size.calc_distance(player.position, boss.position))
    print("which direction would you like to move? \n")
    while direction:
        move = input("up, down, left, right \n")
        if move == "up":
            movement.move(player.position,"up")
            direction = False
        elif move == "down":
            movement.move(player.position,"down")
            direction = False
        elif move == "left":
            movement.move(player.position,"left")
            direction = False
        elif move == "right":
            movement.move(player.position,"right")
            direction = False
        else:
            print("Invalid direction.\n")
    direction = True
    
    battle = encounter.enc_probability(player.position, boss.position)
    enemy = encounter.versus(player.position, boss.position)
    if battle:
        print("You have encountered a(n) %s" % enemy.name)
    while battle:
        battle_move = input("What would you like to do? [1. Attack , 2. Heal]\n")
        if battle_move == 1:
            player.hit(enemy)
            if enemy.health > 0:
                enemy.hit(player)
                if player.health <= 0:
                    battle = False
                    gameplay = False
                    print("You lose.")
            else:
                if enemy.name == boss.name:
                    win = True
                    gameplay = False
                    print("You win!")
                battle = False
        if battle_move == 2:
            player.potion()
            enemy.hit(player)
            if player.health <= 0:
                    battle = False
                    gameplay = False
                    print("You lose.")
    




                










#####
# while enemy.health >= 130:
#     warrior.hit(enemy)
#     print(enemy.health)

# healer.heal(knight)
# print(knight.health)