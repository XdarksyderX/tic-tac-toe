import random
def AIputs(grid_info):
    while True:
        grind_number = len(grid_info) - 1
        row = random.randint(0, grind_number)
        column = random.randint(0, grind_number)
        position = grid_info[row][column]
        if position != "X" and position != "O":
            grid_info[row][column] = "O"
            break
    