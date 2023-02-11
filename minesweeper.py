"""
This is the file which holds all code for the Minesweeper game
"""
import random
import pygame

# Create the dimensions for the minefield interface that will be displayed to the user. Create a dictionary that will
# store all the necessary images for the game

width = height = 512
cell_size = height // 5
images = {}


# Define load images function to loop through list of symbols and set the value to each symbol in the dictionary as its
# corresponding image.

def load_images():
    symbols = ['1', '2', '3', '4', '5', '6', '7', '8', '0', 'Unopened', 'Mine', 'Flag']
    for symbol in symbols:
        images[symbol] = pygame.transform.scale(
            pygame.image.load('/Users/james/Desktop/Python Projects/Minesweeper/Images/' +
                              symbol + '.png'), (cell_size, cell_size))


# Define a function to generate an empty 5x5 grid and then randomly replace each index with either '-' for an empty
# cell or 'mine' for a mine at a ratio of 4:1. Then, check each empty cell to see how many mines are adjacent to
# it and replace '-' with the corresponding integer.

def generate_grid():
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

            grid[row][col] = str(mines)
            mines = 0

    return grid


# Create Minefield class to graphically represent and keep track of the grid.
class Minefield:
    def __init__(self, grid):
        self.grid = grid

    def get_cell(self, row, col):  # Retrieves whatever is in the cell
        return self.grid[row][col]

    def render_grid(self, screen, grid):  # Loops through the minefield and blits corresponding image onto each index.
        for row in range(5):
            for col in range(5):
                symbol = grid[row][col]
                screen.blit(images[symbol], pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size))
        pygame.display.update()


# Define main function to act as the driver for the game. It will create an instance of the Minefield class to act as
# the current game and keep track of user inputs.

def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    load_images()
    game = generate_grid()
    minefield = Minefield(game)  # minefield is now a game instance
    minefield.render_grid(screen, game)  # Grid now loaded
    pygame.display.update()
    running = True
    pygame.display.update()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                col = location[0] // cell_size  # x value of mouse
                row = location[1] // cell_size  # y value of mouse
                cell_selected = minefield.get_cell(row, col)  # Programme recognises which cell the user has clicked on and can act according to what is contained in the cell
                if cell_selected == 'Mine':
                    running = False


main()
