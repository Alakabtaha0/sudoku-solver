import pygame as pg
import sys

# Create window
# Set window title
# make background black
# Set pixels

grid = [
        [{"num": None, "init": False}, {"num": None, "init": False}, {"num": 6, "init": True}, {"num": None, "init": False}, {"num": None, "init": False}, {"num": None, "init": False}, {"num": 5, "init": True}, {"num": None, "init": False}, {"num": 8, "init": True}],
        [{"num": 1, "init": True}, {"num": None, "init": False}, {"num": 2, "init": True}, {"num": 3, "init": True}, {"num": 8, "init": True}, {"num": None, "init": False}, {"num": None, "init": False}, {"num": None, "init": False}, {"num": 4, "init": True}],
        [{"num": None, "init": False}, {"num": None, "init": False}, {"num": None, "init": False}, {"num": 2, "init": True}, {"num": None, "init": False}, {"num": None, "init": False}, {"num": 1, "init": True}, {"num": 9, "init": True}, {"num": None, "init": False}],
        [{"num": None, "init": False}, {"num": None, "init": False}, {"num": None, "init": False}, {"num": None, "init": False}, {"num": 6, "init": True}, {"num": 3, "init": True}, {"num": None, "init": False}, {"num": 4, "init": True}, {"num": 5, "init": True}],
        [{"num": None, "init": False}, {"num": 6, "init": True}, {"num": 3, "init": True}, {"num": 4, "init": True}, {"num": None, "init": False}, {"num": 5, "init": True}, {"num": 8, "init": True}, {"num": 7, "init": True}, {"num": None, "init": False}],
        [{"num": 5, "init": True}, {"num": 4, "init": True}, {"num": None, "init": False}, {"num": 9, "init": True}, {"num": 2, "init": True}, {"num": None, "init": False}, {"num": None, "init": False}, {"num": None, "init": False}, {"num": None, "init": False}],
        [{"num": None, "init": False}, {"num": 8, "init": True}, {"num": 7, "init": True}, {"num": None, "init": False}, {"num": None, "init": False}, {"num": 4, "init": True}, {"num": None, "init": False}, {"num": None, "init": False}, {"num": None, "init": False}],
        [{"num": 2, "init": True}, {"num": None, "init": False}, {"num": None, "init": False}, {"num": None, "init": False}, {"num": 9, "init": True}, {"num": 8, "init": True}, {"num": 4, "init": True}, {"num": None, "init": False}, {"num": 7, "init": True}],
        [{"num": 4, "init": True}, {"num": None, "init": False}, {"num": 9, "init": True}, {"num": None, "init": False}, {"num": None, "init": False}, {"num": None, "init": False}, {"num": 3, "init": True}, {"num": None, "init": False}, {"num": None, "init": False}]
    ]



def game_loop():
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()
    running = True
    SELECTED = None
    # Game Loop
    while running:
        # Check for event
        for event in pg.event.get():
            # Check if user quits
            if event.type == pg.QUIT:
                running = False
                break

            # Check for mouse down
            if event.type == pg.MOUSEBUTTONDOWN:
                # Get the position of the mouse
                x, y = pg.mouse.get_pos()
                if x > 450 or y > 450: continue
                # Floor the position to get the row and column
                row = y // 50
                col = x // 50
                if grid[row][col]['init'] != True: SELECTED = [row, col]
            
            # Check for number input
            if event.type == pg.KEYDOWN and SELECTED is not None:
                # If the key is a number and the cell is not an initial number
                if event.unicode.isdigit() and event.unicode != '0' and grid[SELECTED[0]][SELECTED[1]]['init'] == False:
                    # Change the value of the cell to the number
                    grid[SELECTED[0]][SELECTED[1]]['num'] = int(event.unicode)
                    SELECTED = None

        # RENDERING
        # Update the screen with the new frame
        screen.fill("grey")
        # Each cell is 50x50 pixels
        # Goes through each row
        for row in range(len(grid)):
            # Goes through each column
            for col in range(len(grid[row])):
                # If the cell is selected
                if SELECTED is not None and [row, col] == SELECTED:
                    # Draw a grey rectangle in the selected cell
                    pg.draw.rect(screen, "black", (col * 50 +1, row * 50 +1, 50, 50))
                    pg.draw.rect(screen, "grey", (col * 50, row * 50, 49, 49))
                    # Create a font object to draw the number
                    font = pg.font.Font(None, 36)
                    # if it's not None, draw the number else draw nothing
                    screen.blit(font.render(str(grid[row][col]['num']), True, "black"), (col * 50 + 17, row * 50 + 13)) if grid[row][col]['num'] is not None else None
                    continue
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
        clock.tick(30)
    return

# Main Function
def main():
    # Sudoku Grid
    # Set object so that we can keep track of the initial numbers and no changes can be made
    

    # Initialize Pygame
    pg.init()
    pg.display.set_caption("Sudoku Solver")
    
    game_loop()
    

    pg.quit()


if __name__ == "__main__":
    main()
    sys.exit(0)
