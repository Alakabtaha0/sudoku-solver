import pygame as pg
import sys

# Create window
# Set window title
# make background black
# Set pixels


# Main Function
def main():
    grid = [
        [0, 0, 6, 0, 0, 0, 5, 0, 8],
        [1, 0, 2, 3, 8, 0, 0, 0, 4],
        [0, 0, 0, 2, 0, 0, 1, 9, 0],
        [0, 0, 0, 0, 6, 3, 0, 4, 5],
        [0, 6, 3, 4, 0, 5, 8, 7, 0],
        [5, 4, 0, 9, 2, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 4, 0, 0, 0],
        [2, 0, 0, 0, 9, 8, 4, 0, 7],
        [4, 0, 9, 0, 0, 0, 3, 0, 0],
    ]

    # Initialize Pygame
    pg.init()
    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption("Sudoku Solver")
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
                print(f"x: {x}, y: {y}")
                # Floor the position to get the row and column
                row = y // 50
                col = x // 50
                SELECTED = [row, col]
                print(f"SELECTED:: {SELECTED}")
                print(grid[row][col])

        # RENDERING
        # Update the screen with the new frame
        screen.fill("grey")
        # Each cell is 50x50 pixels
        # Goes through each row
        for row in range(len(grid)):
            # Goes through each column
            for col in range(len(grid[row])):
                if SELECTED is not None and [row, col] == SELECTED:
                    # Draw a grey rectangle in the selected cell
                    pg.draw.rect(screen, "grey", (col * 50, row * 50, 50, 50))
                    # Create a font object to draw the number
                    font = pg.font.Font(None, 36)
                    # Render the number
                    text = font.render(str(grid[row][col]), True, "black")
                    # Draw the number ontop of the white rectangle along with the offset
                    screen.blit(text, (col * 50 + 17, row * 50 + 13))
                    continue
                # If the value is 0, draw a black rectangle
                if grid[row][col] != 0:
                    # Draw a white rectangle which is the background
                    pg.draw.rect(screen, "white", (col * 50, row * 50, 50, 50))
                    # Create a font object to draw the number
                    font = pg.font.Font(None, 36)
                    # Render the number
                    text = font.render(str(grid[row][col]), True, "black")
                    # Draw the number ontop of the white rectangle along with the offset
                    screen.blit(text, (col * 50 + 17, row * 50 + 13))
                else:
                    # Draw a black rectangle
                    pg.draw.rect(screen, "black", (col * 50, row * 50, 50, 50))
                    font = pg.font.Font(None, 36)

        # Draw the new frame
        pg.display.flip()

        # Frame rate
        clock.tick(30)

    pg.quit()


if __name__ == "__main__":
    main()
    sys.exit(0)
