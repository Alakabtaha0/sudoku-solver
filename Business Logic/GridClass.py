class Grid:
    # Pass a grid or just create an empty grid
    def __init__(self, grid=None):
        self.grid = grid or [
    [
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
    ],
    [
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
    ],
    [
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
    ],
    [
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
    ],
    [
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
    ],
    [
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
    ],
    [
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
    ],
    [
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
    ],
    [
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
        {"num": None, "init": False},
    ],
]

    def get_cell(self, row, col):
        return self.grid[row][col]

    def set_cell(self, row, col, value):
        self.grid[row][col]["num"] = value

    def print_grid(self):
        for row in self.grid:
            print(row)