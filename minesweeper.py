"""
===================================================== Imports ==========================================================
"""

import random
import pygame

"""
===================================================== Graphics =========================================================
"""

# Create the dimensions for the minefield interface that will be displayed to the user. Create a dictionary that will
# store all the necessary images for the game.

width = height = 512
cell_size = height // 5
images = {}
screen = pygame.display.set_mode((width, height))


# Define load images function to loop through list of symbols and set the value to each symbol in the dictionary as its
# corresponding image.

def load_images():
    symbols = [1, 2, 3, 4, 5, 6, 7, 8, 0, 'Unopened', 'Mine', 'Flag']
    for symbol in symbols:
        images[symbol] = pygame.transform.scale(
            pygame.image.load('/Users/james/Desktop/Python Projects/Minesweeper/Images/' +
                              str(symbol) + '.png'), (cell_size, cell_size))


"""
================================================= Game mechanics =======================================================
"""


# Create the Minefield class that will be responsible for keeping track of all necessary information about the grid,
# e.g. starting grid, which cells have been opened by the user, etc.

class Minefield:
    def __init__(self):
        self.grid = self.generate_grid()
        self.checked = set()

    # Define the generate grid method to create an empty grid and randomly populate it with mines upon game start. The
    # function will check each grid cell to see how many mines are adjacent to that cell and then replace the '-'
    # placeholder with the corresponding integer.

    def generate_grid(self):
        grid_sides = 5
        grid = [[None] * grid_sides for _ in range(grid_sides)]
        rows = len(grid)
        for row in range(rows):
            cols = len(grid[row])
            for col in range(cols):
                rng = random.randint(1, 5)
                if rng == 5:
                    grid[row][col] = "Mine"
                else:
                    grid[row][col] = "-"
        mines = 0
        rows = len(grid)
        for row in range(rows):
            cols = len(grid[row])
            for col in range(cols):
                if grid[row][col] == "Mine":  # Skip if contains mine
                    continue
                if row > 0 and col > 0 and grid[row - 1][col - 1] == "Mine":  # Check north-west
                    mines += 1
                if row > 0 and grid[row - 1][col] == "Mine":  # Check north
                    mines += 1
                if row > 0 and col < 4 and grid[row - 1][col + 1] == "Mine":  # Check north-east
                    mines += 1
                if col > 0 and grid[row][col - 1] == "Mine":  # Check west
                    mines += 1
                if col < 4 and grid[row][col + 1] == "Mine":  # Check east
                    mines += 1
                if row < 4 and col > 0 and grid[row + 1][col - 1] == "Mine":  # Check south-west
                    mines += 1
                if row < 4 and grid[row + 1][col] == "Mine":  # Check south
                    mines += 1
                if row < 4 and col < 4 and grid[row + 1][col + 1] == "Mine":  # Check south-east
                    mines += 1

                # Convert - to number stored in mines and reset counter

                grid[row][col] = mines
                mines = 0

        return grid

    # Define the check cell method to resolve and keep track of each user move. If the user click on a cell containing a
    # bomb, return False. The driver section will handle what happens after the loss. If the cell contains a number > 0,
    # return True. If the cell contains a 0, return True AND reveal every adjacent cell which is not a bomb. Blit
    # correct image in all cases.
    def check_cell(self, row, col):
        self.checked.add((row, col))
        if self.grid[row][col] == 'Mine':
            screen.blit(images['Mine'], pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size))
            pygame.display.update()
            return False
        elif self.grid[row][col] > 0:  # Not mine or empty cell
            screen.blit(images[self.grid[row][col]],
                        pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size))
            pygame.display.update()
            return True
        else:  # Empty cells
            for r in range(row - 1, row + 2):
                for c in range(col - 1, col + 2):
                    if r < 0 or c < 0 or r > 4 or c > 4:
                        continue  # Do not check out of bounds
                    if (r, c) in self.checked:
                        continue  # Do not check cells that have already been opened
                    if self.grid[r][c] != 'Mine':
                        self.checked.add((r, c))
                        self.check_cell(r, c)  # Open all adjacent cells that are not mines
                        screen.blit(images[self.grid[row][col]],
                                    pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size))
                        pygame.display.update()

            return True


"""
=================================================== Driver =============================================================
"""


# Define render starting grid function to blit unopened cell images on to each cell in the grid. This gives us the
# starting minefield graphic

def render_starting_grid(game):
    rows = len(game)
    for row in range(rows):
        cols = len(game[row])
        for col in range(cols):
            screen.blit(images["Unopened"], pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size))
    pygame.display.update()


# Define main function to act as the driver for the game. It will create an instance of the Minefield class to act as
# the current game and handle inputs.

def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    load_images()
    game = Minefield()  # Game now initialised
    render_starting_grid(game.grid)  # Starting grid loaded
    running = True
    while running:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            row = y // cell_size
            col = x // cell_size
            game.check_cell(row, col)  # Game checks the cell that the user has clicked on and handles logic


main()
