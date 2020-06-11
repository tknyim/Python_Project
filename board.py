def gen_board(width,length):
    board = []
    row = []
    for x in range (0,width):
        row.append(x)
    for y in range (0,length):
        board.append(row)
    return board
