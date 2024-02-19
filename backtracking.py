import time
import pygame as pg
import sys
from grid import grid
# Backtracking algorithm
# Run this file to see the backtracking algorithm in action

# Initialize Pygame
pg.init()
pg.display.set_caption("Sudoku Solver")
screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()

def render_window():
    
    
        # Check for event
        for event in pg.event.get():
            # Check if user quits
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)
                break

           
        # RENDERING
        # Update the screen with the new frame
        screen.fill("grey")
        # Each cell is 50x50 pixels
        # Goes through each row
        for row in range(len(grid)):
            # Goes through each column
            for col in range(len(grid[row])):
                # Draw the grid lines
                if row % 3 == 0 and row != 0:
                    pg.draw.line(screen, "black", (0, row * 50), (600, row * 50), 2)
                if col % 3 == 0 and col != 0:
                    pg.draw.line(screen, "black", (col * 50, 0), (col * 50, 450), 2)
                # If the cell is selected
               
                # If the value is 0, draw a black rectangle
                if grid[row][col]['num'] != None:
                    # Draw a white rectangle which is the background
                    pg.draw.rect(screen, "black", (col * 50 +1, row * 50 +1, 50, 50))
                    pg.draw.rect(screen, "white", (col * 50, row * 50, 49, 49))
                    # Create a font object to draw the number
                    font = pg.font.Font(None, 36)
                    # Render the number
                    text = font.render(str(grid[row][col]['num']), True, "black")
                    # Draw the number ontop of the white rectangle along with the offset
                    screen.blit(text, (col * 50 + 17, row * 50 + 13))
                else:
                    # Draw a white rectangle
                    pg.draw.rect(screen, "black", (col * 50 +1, row * 50 +1, 50, 50))
                    pg.draw.rect(screen, "white", (col * 50, row * 50, 49, 49))
                    

        # Draw the new frame
        pg.display.flip()
        # Frame rate
        clock.tick(60)
    

# Solve function
def solve(g):
    time.sleep(0.05)
    render_window()
    find = find_empty(g)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(g, i, (row, col)):
            g[row][col]["num"] = i
            if solve(g):
                return True

            g[row][col]["num"] = None

    return False


# Check if valid
def valid(g, num, pos):
    # Check row
    for i in range(len(g[pos[0]])):
        if g[pos[0]][i]["num"] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(g)):
        if g[i][pos[1]]["num"] == num and pos[0] != i:
            return False

    # Check 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if g[i][j]["num"] == num and (i, j) != pos:
                return False
    return True


# Find an empty cell
def find_empty(g):
    for row in range(len(g)):
        for col in range(len(g[row])):
            if g[row][col]["num"] == None:
                return (row, col)  # This is the position of the empty cell


solve(grid)
pg.quit()
sys.exit(0)