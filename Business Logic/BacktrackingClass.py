

class Backtracking():

    def __init__(self, grid) -> None:
        self.solved_grid = self.solve(grid)
        if self.solved_grid is not None:
            print("Solution found:")
        else:
            print("No solution found.")

    # Find the position of the empty cell
    def find_empty(self, grid):
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col]["num"] == None:
                    return (row, col)  # This is the position of the empty cell
            
    # Solve function
    def solve(self, grid):
        find = self.find_empty(grid)
        if not find:
            return grid
        else:
            row, col = find

        for i in range(1, 10):
            if self.valid(grid, i, (row, col)):
                grid[row][col]["num"] = i
                if self.solve(grid):
                    return grid

                grid[row][col]["num"] = None

        return None  

    # Check if valid
    def valid(self, grid, num, pos):
        # Check row
        for i in range(len(grid[pos[0]])):
            if grid[pos[0]][i]["num"] == num and pos[1] != i:
                return False

        # Check column
        for i in range(len(grid)):
            if grid[i][pos[1]]["num"] == num and pos[0] != i:
                return False

        # Check 3x3 box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if grid[i][j]["num"] == num and (i, j) != pos:
                    return False
        return True