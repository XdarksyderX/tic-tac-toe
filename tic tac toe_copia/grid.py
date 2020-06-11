#ESTA FUNCIÓN CREA EL NÚMERO DE GRILLA
def grid_number():
    while True:    
        try:
            grid_number = int(input("Ingrese el número de grilla: "))
            break
        except:
            print("Ingrese un número entero")
    return grid_number 


#ESTA FUNCIÓN CREA LA GRILLA DE INFORMACIÓN
def createGrid(grid_number):
    grid_info = [["*" for x in range(grid_number)] for y in range(grid_number)] 
    return grid_info
#ESTA FUNCIÓN IMPRIME LA GRILLA EN BASE A LA INFORMACIÓN
def printGrid(grid_info):
    for i in grid_info:
        for j in i:
            print(j, end="\t\t")
        print("\n")



#prueba = createGrid(4)
#printGrid(prueba)
#prueba[1][1] = 2

#print(prueba)