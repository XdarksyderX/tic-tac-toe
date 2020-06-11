import random
import grid, data_enter, tester, AI
if __name__ == '__main__':
    def main():
        grid_number = grid.grid_number()
        grid_info = grid.createGrid(grid_number)
        grid.printGrid(grid_info)
        puts = 0
        while puts <= grid_number ** 2:
            try:
                row = int(input("FILA: "))
                column = int(input("COLUMNA: "))

            except:
                print("Posicón no valida")
                continue
            data_enter.data_enter(grid_info, row, column) 
            puts += 1
            if puts == 9:
                break

            testerer1 = tester.global_tester(grid_info, grid_number)
            if testerer1 == "WIN" or testerer1 == "LOSE":
                break 
                grid.printGrid(grid_info)

            AI.AIputs(grid_info)

            
            grid.printGrid(grid_info)
            testerer2 = tester.global_tester(grid_info, grid_number)

            if testerer2 == "WIN" or testerer2 == "LOSE":
                break 
    main()