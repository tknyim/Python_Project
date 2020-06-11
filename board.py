import random

def gen_board(width,length):
    board = []
    row = []
    for x in range (0,width):
        row.append(x)
    for y in range (0,length):
        board.append(row)
    return board



def calc_distance(main_char, boss):
    distance = (boss.x-main_char.x) + (boss.y-main_char.y)
    if(distance < 0):
        distance = distance * -1
    return distance
   