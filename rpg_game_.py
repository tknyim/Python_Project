import board
from game_stats import Knight, Warrior, Healer, Enemy
knight = Knight("Kevin", {"x":10,"y":100})
warrior = Warrior("Jim", {"x":10,"y":100})
healer = Healer("Pam", {"x":10,"y":100})
enemy = Enemy("Dwight", {"x":10, "y":100})
enemy2 = Enemy("Michael", {"x":10, "y":100})


# while enemy.health >= 130:
#     warrior.hit(enemy)
#     print(enemy.health)

# healer.heal(knight)
# print(knight.health)

game_board = board.gen_board(6,6)
print(game_board)
print("\n\n\n============================")
print("%s has encountered %s!" % (warrior.name, enemy.name))
print("============================")
while enemy.health > 0 and warrior.health > 0:
        print("\nYou:\n HP: %d // ATK: %d \n" % (warrior.health, warrior.attack))
        print("Goblin:\n HP:%d // ATK: %d " % (enemy.health, enemy.attack))
        print()
        print("What do you want to do?")
        print("1.) Attack")
        print("2.) Drink a potion")
        print("3.) Run")
        print(">> ",)
        user_input = input()
        if user_input == "1":
            warrior.hit(enemy)
            print("\n%s did %d damage to %s." % (warrior.name, warrior.attack, enemy.name))
            if enemy.health <= 0:
                print("\nYou have won!\n")
        elif user_input == "2":
            hp_msg = warrior.potion(warrior)
            print("\n%s drank a potion and recovered %s health." % (warrior.name,hp_msg))
        elif user_input == "3":
            print("\nYou ran away safely.")
            break
        else:
            print("Invalid input %r" % user_input)

        if enemy.health > 0:
            enemy.hit(warrior)
            print("%s does %d damage to %s." % (enemy.name, enemy.attack, warrior.name))
            if warrior.health <= 0:
                print("\nYou are dead.\n")