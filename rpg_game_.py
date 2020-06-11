import board
from game_stats import Knight, Warrior, Healer, Mob, Enemy, Semi_Boss, Boss
knight = Knight("Darryl", {"x":1,"y":2})
warrior = Warrior("Jim", {"x":1,"y":2})
white_mage = Healer("Pam", {"x":1,"y":2})
mob = Mob("Andy", {"x":1,"y":2})
enemy = Enemy("Dwight", {"x":1,"y":2})
small_boss = Semi_Boss("Michael", {"x":1,"y":2})
boss = Boss("Robert California", {"x":1,"y":2})


game_board = board.gen_board(6,6)
print(game_board)



nextStep = True

while nextStep:
    print("\nChoose a character: [ 1. Warrior   2. Knight   3. White Mage ]")
    select = int(input(">> ", ))
    if select != 1 and select != 2 and select != 3:
        print("\nNot a character.")

    elif select == 1:
        print("\nYou have chosen warrior as your character!")
        
        print("\n\n\n============================")
        print("%s has encountered %s!" % (warrior.name, enemy.name))
        print("============================")
        while enemy.health > 0 and warrior.health > 0:
                print()
                print("=======================")
                print("What do you want to do?")
                print("1.) Attack")
                print("2.) Drink a potion")
                print("3.) Run")
                print("=======================",)
                print("%s:\n [HP: %d // ATK: %d // DEF: %d]" % (warrior.name, warrior.health, warrior.attack, warrior.defense))
                print("%s:\n [HP: %d // ATK: %d // DEF: %d]" % (enemy.name, enemy.health, enemy.attack, enemy.defense))
                print("=======================")
                user_input = input(">> ")
                
                if user_input == "1":
                    enemy.health -= (warrior.attack - enemy.defense)
                    print("\n%s did %d damage to %s." % (warrior.name, warrior.attack, enemy.name))
                    if enemy.health <= 0:
                        print("\nYou have won!\n")
                        exit()


                elif user_input == "2":
                    hp_msg = warrior.potion(warrior)
                    print("\n%s drank a potion and recovered %s health." % (warrior.name,hp_msg))


                elif user_input == "3":
                    print("\nYou ran away safely.\n")
                    exit()
                else:
                    print("Invalid option %r" % user_input)

                if enemy.health > 0:
                    warrior.health -= (enemy.attack - warrior.defense)
                    print("%s does %d damage to %s." % (enemy.name, enemy.attack, warrior.name))
                if warrior.health <= 0:
                    print("\nYou are dead.\n")     

    elif select == 2:
        print("\nYou have chosen Knight as your character!")

        print("\n\n\n============================")
        print("%s has encountered %s!" % (knight.name, enemy.name))
        print("============================")
        while enemy.health > 0 and knight.health > 0:
                print()
                print("=======================")
                print("What do you want to do?")
                print("1.) Attack")
                print("2.) Drink a potion")
                print("3.) Run")
                print("=======================",)
                print("%s:\n [HP: %d // ATK: %d // DEF: %d]" % (knight.name, knight.health, knight.attack, knight.defense))
                print("%s:\n [HP: %d // ATK: %d // DEF: %d]" % (enemy.name, enemy.health, enemy.attack, enemy.defense))
                print("=======================")
                user_input = input(">> ")
                
                if user_input == "1":
                    enemy.health -= (knight.attack - enemy.defense)
                    print("\n%s did %d damage to %s." % (knight.name, knight.attack, enemy.name))
                    if enemy.health <= 0:
                        print("\nYou have won!\n")
                        exit()


                elif user_input == "2":
                    hp_msg = knight.potion(knight)
                    print("\n%s drank a potion and recovered %s health." % (knight.name,hp_msg))


                elif user_input == "3":
                    print("\nYou ran away safely.\n")
                    exit()
                else:
                    print("Invalid option %r" % user_input)

                if enemy.health > 0:
                    knight.health -= (enemy.attack - knight.defense)
                    print("%s does %d damage to %s." % (enemy.name, enemy.attack, knight.name))
                if knight.health <= 0:
                    print("\nYou are dead.\n")


    elif select == 3:
        print("\nYou have chosen White Mage as your character!")

        print("\n\n\n============================")
        print("%s has encountered %s!" % (white_mage.name, enemy.name))
        print("============================")
        while enemy.health > 0 and white_mage.health > 0:
                print()
                print("=======================")
                print("What do you want to do?")
                print("1.) Attack")
                print("2.) Heal")
                print("3.) Run")
                print("=======================",)
                print("%s:\n [HP: %d // ATK: %d // DEF: %d]" % (white_mage.name, white_mage.health, white_mage.attack, white_mage.defense))
                print("%s:\n [HP: %d // ATK: %d // DEF: %d]" % (enemy.name, enemy.health, enemy.attack, enemy.defense))
                print("=======================")
                user_input = input(">> ")
                
                if user_input == "1":
                    enemy.health -= (warrior.attack - enemy.defense)
                    print("\n%s did %d damage to %s." % (white_mage.name, white_mage.attack, enemy.name))
                    if enemy.health <= 0:
                        print("\nYou have won!\n")
                        exit()


                elif user_input == "2":
                    white_mage.heal(white_mage)
                    print("\n%s used heal and recovered by %s health." % (white_mage.name,white_mage.heal))


                elif user_input == "3":
                    print("\nYou ran away safely.\n")
                    exit()
                else:
                    print("Invalid option %r" % user_input)

                if enemy.health > 0:
                    white_mage.health -= (enemy.attack - white_mage.defense)
                    print("%s does %d damage to %s." % (enemy.name, enemy.attack, white_mage.name))
                if white_mage.health <= 0:
                    print("\nYou are dead.\n")

                










#####
# while enemy.health >= 130:
#     warrior.hit(enemy)
#     print(enemy.health)

# healer.heal(knight)
# print(knight.health)