def horizontal_tester(grid_info, element):
    confirmer = False
    for fila in grid_info:
        count = 0
        for columna in fila:
            if columna == element:
                count += 1

            if count == len(fila):
                confirmer = True
                break
    if confirmer:
        return True

def vertical_tester(grid_info, element, grid_number):
    confirmer = False
    for vertical in range(grid_number):
        count = 0
        for fila in grid_info:
            if fila[vertical] == element:
                count += 1

            if count == grid_number:
                confirmer = True
                return confirmer

def diagonal_1_tester(grid_info, element, grid_number):
    confirmer = False
    contador = 0
    for j in range(grid_number):
        if grid_info[j][j] == "X":
            contador += 1
    if contador == grid_number:
        confirmer = True
        return confirmer

def diagonal_2_tester(grid_info, element, grid_number):
    confirmer = False
    contador = 0
    for j in range(grid_number):
        j += 1
        if grid_info[j - 1][-j] == "X":
            contador += 1
    if contador == grid_number:
        confirmer = True
        return confirmer

def diaonal_tester(grid_info, element, grid_number):
    diagonal_1 = diagonal_1_tester(grid_info, element, grid_number)
    diagonal_2 = diagonal_2_tester(grid_info, element, grid_number)
    if diagonal_1 or diagonal_2:
        return True                

def global_testerX(grid_info, grid_number):
    tester1_X = horizontal_tester(grid_info, "X")
    tester2_X = vertical_tester(grid_info, "X", grid_number)
    tester3_X = diaonal_tester(grid_info, "X", grid_number)

    if tester1_X or tester2_X or tester3_X:
        return True



def global_testerO(grid_info, grid_number):
    tester1_O = horizontal_tester(grid_info, "O")
    tester2_O = vertical_tester(grid_info, "O", grid_number)
    tester3_O = diaonal_tester(grid_info, "O", grid_number)
    
    if tester1_O or tester2_O or tester3_O:
        return True

def global_tester(grid_info, grid_number):
    tester_X = global_testerX(grid_info, grid_number)
    tester_O = global_testerO(grid_info, grid_number)

    if tester_X:
        print("Has ganado")
        player_winner = "WIN"
        return player_winner
    
    elif tester_O:
        print("Has ganado")
        player_winner = "LOSE"
        return player_winner

