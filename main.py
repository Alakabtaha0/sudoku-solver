from VisionClass import Vision
from GridClass import Grid
from BacktrackingClass import Backtracking
import sys

def main():
    vision = Vision('assets/1.JPG', 'models/model.h5')
    new_grid_values = vision.process_image()
    # Convert the 1D list of values to a 2D list
    new_grid = []
    new_row = []
    for value in new_grid_values:
        new_row.append({"num": None if value == 0 else value, "init": value != 0})
        if len(new_row) == 9:
            new_grid.append(new_row)
            new_row = []

    # grid = Grid(new_grid)  
               
    # Solve the sudoku grid
    grid = Backtracking(new_grid)

if __name__ == "__main__":
    main()
    sys.exit(0)