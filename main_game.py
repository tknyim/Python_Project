import map_size
import movement
import encounter
import random
from game_stats import Knight, Warrior, H, Bahamut


#Generates the dimensions of the map for the game
game_board = map_size.gen_board(6,6)
print(game_board)
nextStep = False

#User's name
player = input("\n\nWhat is your name? \n>> ")
position = map_size.starting_position(map_size)
boss = Bahamut("[BOSS] Bahamut" ,position[1])

#Character selction
while nextStep == False:
    print("\nChoose a character: [ 1. \u001b[33mWarrior of Light\u001b[0m   2. \u001b[33mDark Knight\u001b[0m ]")
    select = int(input(">> "))
    if select == 1:
        player = Warrior(player,position[0])
        print("\n\u001b[33mWarrior of Light selected\u001b[0m\n")
        nextStep = True

    elif select == 2:
        player = Knight(player,position[0])
        print("\n\u001b[33mDark Knight selected\u001b[0m\n")
        nextStep = True

    elif select == 420:
        player = H(player,position[0])
        print("\n\u001b[36mA hidden character was selected???\u001b[0m\n")    
        nextStep = True
    else:
        print("\n\u001b[31mNot a character.\u001b[0m")


gameplay = True
win = False
battle = False
direction = True
step_count = 0
score = 0



#Directions input
while gameplay:
    print("Your position is \u001b[32mx: %s , y: %s\u001b[0m \n" % (player.position.x, player.position.y))
    print("Your distance between the boss is \u001b[32m%s\u001b[0m \n" % map_size.calc_distance(player.position, boss.position))
    print("which direction would you like to move? \n")
    while direction:
        step_count += 1
        move = input("[\u001b[36mup, down, left, right\u001b[0m] \n>> ")
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
            print("\u001b[31mInvalid direction.\u001b[0m\n")
    direction = True
    #Players starting position and distance away from the boss
    battle = encounter.enc_probability(player.position, boss.position)
    enemy = encounter.versus(player.position, boss)
    #Battle mechanic
    if battle:
        print(chr(27) + "[2J")
        print("\u001b[35mYou have encountered a %s \u001b[0m\n" % enemy.name)
    while battle:
        print("%s:\n [HP: \u001b[32m%d\u001b[0m // ATK: \u001b[32m%d\u001b[0m // DEF: \u001b[32m%d\u001b[0m // Potion(s): \u001b[32m%d\u001b[0m]" % (player.name, player.health, player.attack, player.defense, player.pot))
        print("%s:\n [HP: \u001b[32m%d\u001b[0m // ATK: \u001b[32m%d\u001b[0m // DEF: \u001b[32m%d\u001b[0m]\n" % (enemy.name, enemy.health, enemy.attack, enemy.defense))
        battle_move = input("What would you like to do? [1. \u001b[36mAttack\u001b[0m , 2. \u001b[36mHeal\u001b[0m] \n>> ")
        if battle_move == "1":
            enemy.health -= (player.attack - enemy.defense)
            print("\n\u001b[33m%s\u001b[0m did \u001b[32m%d\u001b[0m damage to \u001b[35m%s\u001b[0m." % (player.name, player.attack, enemy.name))
            if enemy.health <= 0:
                print("\nYou defeated a \u001b[35m%s\u001b[0m!\n" % enemy.name)
                player.pot += 1
                print("\n\u001b[32mYou have obtained a potion!\u001b[0m")
                score += enemy.score
                battle = False
                
                
                if boss.health <= 0:
                    win = True
                    gameplay = False
                    print("\n\u001b[36mCongratulations you win!\u001b[0m \n")
                    print("Your final score is \u001b[32m%d\u001b[0m and total steps are \u001b[32m%d\u001b[0m.\n" % (score, step_count))
                    

            else: 
                player.health -= (enemy.attack - player.defense)
                print("\u001b[35m%s\u001b[0m does \u001b[31m%d\u001b[0m damage to \u001b[33m%s\u001b[0m." % (enemy.name, enemy.attack, player.name))
            
                
            if  player.health <= 0:
                battle = False
                gameplay = False
                print("\n\u001b[31mYou are dead.\u001b[0m\n")
                print("Your final score is \u001b[32m%d\u001b[0m and total steps are \u001b[32m%d\u001b[0m.\n" % (score, step_count))

        elif battle_move == "2":
            if player.pot > 0:
                player.health = (player.health + 20)
                player.pot -= 1
                print("\n\u001b[32m%s drank a potion and recovered by 20.\u001b[0m" % player.name)
            player.health -= (enemy.attack - player.defense)
            print("\u001b[35m%s\u001b[0m does \u001b[31m%d\u001b[0m damage to \u001b[33m%s\u001b[0m." % (enemy.name, enemy.attack, player.name))
            if player.pot <= 0:
                print("\n\u001b[31mYou're out of potion(s)\u001b[0m. \n")