from .VisionClass import Vision
from .GridClass import Grid
from .BacktrackingClass import Backtracking
# import sys
import os

script_dir = os.path.dirname(__file__)
model_path = os.path.join(script_dir, 'models', 'model.h5')
temp_img = os.path.join(script_dir, 'assets', '1.JPG')

def process_image(image):
    vision = Vision(image, model_path)
    new_grid_values = vision.process_image()
    # Convert the 1D list of values to a 2D list
    new_grid = []
    new_row = []
    for value in new_grid_values:
        new_row.append({"num": None if value == 0 else value, "init": value != 0})
        if len(new_row) == 9:
            new_grid.append(new_row)
            new_row = []

    grid = Grid(new_grid)
    return grid
               
    # Solve the sudoku grid
    # grid = Backtracking(new_grid)


# if __name__ == "__main__":
#     x = main(temp_img)
#     print(x.return_grid())
#     sys.exit(0)
