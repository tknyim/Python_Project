import random

def gen_board(width,length):
    board = []
    row = []
    for x in range (0,width):
        row.append(x)
    for y in range (0,length):
        board.append(row)
    return board

def starting_position(board):
    main_char = {"x":random.randint(0,5),"y":random.randint(0,5)}
    distance = 0
    while(distance <= 3):
        boss = {"x":random.randint(0,5),"y":random.randint(0,5)}
        distance = calc_distance(main_char,boss)

def calc_distance(main_char, boss):
    distance = (boss.x-main_char.x) + (boss.y-main_char.y)
    if(distance < 0):
        distance = distance * -1
    return distance
   
