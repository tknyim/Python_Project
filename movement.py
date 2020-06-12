def move(position, direction):
    turn = False
    if direction == "up":
        if position.y -1 < 0:
            print("Cannot move in this direction.")
        else:
            position.y -= 1
            turn = True
    
    if direction == "down":
        if position.y + 1 > 5:
            print("Cannot move in this direction.")
        else:
            position.y += 1
            turn = True
    
    if direction == "left":
        if position.x - 1 < 0:
            print("Cannot move in this direction.")
        else:
            position.x -= 1
            turn = True
    
    if direction == "right":
        if position.x + 1 > 5:
            print("Cannot move in this direction.")
        else:
            position.x += 1
            turn = True
    return turn


