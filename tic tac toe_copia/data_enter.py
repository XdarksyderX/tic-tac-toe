def data_enter(grid_info, row, col):
    row -= 1
    col -= 1
    
    try:
        column = grid_info[row][col]

        if column != "X" or column != "O":
            grid_info[row][col] = "X" 
        else:
            print("Esa posición ya está introducida")

    except:
        print("Información mal introducida")    
