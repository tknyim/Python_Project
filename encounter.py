import random
import map_size
from game_stats import Gremlin, Werewolf, Chimera, Bahamut

#Probability of encountering weak-strong monsters
def versus(main_char, boss):
    distance = map_size.calc_distance(main_char, boss.position)
    monster = "Enemy"

    if distance >= 7:
        monster = Gremlin("Tonberry", main_char)
    elif distance < 7 and distance >= 3:
        monster = Werewolf("Werewolf", main_char)
    elif distance < 3 and distance > 0:
        monster = Chimera("Chimera", main_char)
    elif distance == 0:
        monster = boss
    else:
        print("Cannot move in this direction ")
    return monster

def enc_probability(main_char, boss):
    distance = map_size.calc_distance(main_char, boss)
    if random.randint(1,10) >= distance:
        return True
    else: 
        return False

# def potion_drop():
#     drop_potion = random.randint(1,5)
#     if drop_potion >= 3:
#         return True
#     else:
#         return False

