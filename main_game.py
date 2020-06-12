import map_size
import movement
import encounter
import random
from game_stats import Knight, Warrior, Bahamut



game_board = map_size.gen_board(6,6)
print(game_board)
nextStep = False

player = input("\n\nWhat is your name? \n>> ")
position = map_size.starting_position(map_size)
boss = Bahamut("Bahamut" ,position[1])

while nextStep == False:
    print("\nChoose a character: [ 1. Warrior of Light   2. Dark Knight ]")
    select = int(input(">> "))
    if select == 1:
        player = Warrior(player,position[0])
        print("\n Warrior of Light selected")
        nextStep = True

    elif select == 2:
        player = Knight(player, position[0])
        print("\n Dark Knight selected")
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
        move = input("[up, down, left, right] \n>> ")
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
    enemy = encounter.versus(player.position, boss)
    if battle:
        print("You have encountered a(n) %s \n" % enemy.name)
    while battle:
        print("%s:\n [HP: %d // ATK: %d // DEF: %d]" % (player.name, player.health, player.attack, player.defense))
        print("%s:\n [HP: %d // ATK: %d // DEF: %d]" % (enemy.name, enemy.health, enemy.attack, enemy.defense))
        battle_move = input("What would you like to do? [1. Attack , 2. Heal] \n>> ")
        if battle_move == "1":
            enemy.health -= (player.attack - enemy.defense)
            print("\n%s did %d damage to %s." % (player.name, player.attack, enemy.name))
            if enemy.health <= 0:
                print("\nYou defeated a %s!\n" % enemy.name)
                battle = False
                
                if boss.health <= 0:
                    win = True
                    gameplay = False
                    print("Congraulations you win! \n")
                    

            else: 
                player.health -= (enemy.attack - player.defense)
                print("%s does %d damage to %s." % (enemy.name, enemy.attack, player.name))
            
                
            if  player.health <= 0:
                battle = False
                gameplay = False
                print("\nYou are dead.\n")

        elif battle_move == "2":
            player.health = (player.health + 30)
            print("\n%s drank a potion and recovered by 30." % player.name)
            player.health -= (enemy.attack - player.defense)
            print("%s does %d damage to %s." % (enemy.name, enemy.attack, player.name))