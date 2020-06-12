import random

def gen_board(width,length):
    board = []
    row = []
    for x in range (0,width):
        row.append(x)
    for y in range (0,length):
        board.append(row)
    return board

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def starting_position(board):
    main_char = Position(random.randint(0,5),random.randint(0,5))
    distance = 0
    while(distance <= 3):
        boss = Position(random.randint(0,5),random.randint(0,5))
        distance = calc_distance(main_char,boss)
    return(main_char,boss)

def calc_distance(main_char, boss):
    x = (boss.x-main_char.x)
    if x < 0:
        x = x * -1

    y = (boss.y-main_char.y)
    if y < 0:
        y = y * -1
    distance = x+y
    return distance
   
