# Create an empty 5x5 grid and then randomly replace each index with either - or # at a ratio of 4:1

grid_sides = 5
empty_grid = [[None] * grid_sides for x in range(grid_sides)]

import random

rows = len(empty_grid)
for row in range(rows):
    cols = len(empty_grid[row])
    for col in range(cols):
        rng = random.randint(1,5)
        if rng == 5:
            empty_grid[row][col] = "#"
        else:
            empty_grid[row][col] = "-"

mine_grid = empty_grid

# Create a function to check if mine is adjacent and increase counter but excludes out of bounds checks

mines = 0
rows = len(mine_grid)
for row in range(rows):
    cols = len(mine_grid[row])
    for col in range(cols):
        
        # Skip if contains mine
            
        if mine_grid[row][col] == "#":
            continue

        # North-west 

        if row > 0 and col > 0 and mine_grid[row-1][col-1] == "#":
            mines += 1

        # North

        if row > 0 and mine_grid[row-1][col] == "#":
            mines += 1

        # North-east

        if row > 0 and col < 4 and mine_grid[row-1][col+1] == "#":
            mines += 1

        # West

        if col > 0 and mine_grid[row][col-1] == "#":
            mines += 1

        # East 

        if col < 4 and mine_grid[row][col+1] == "#":
            mines += 1

        # South-west 

        if row < 4 and col > 0 and mine_grid[row+1][col-1] == "#":
            mines += 1

        # South

        if row < 4 and mine_grid[row+1][col] == "#":
            mines += 1

        # South-east 

        if row < 4 and col < 4 and mine_grid[row+1][col+1] == "#":
            mines += 1

        # Convert - to number stored in mines and reset counter

        mine_grid[row][col] = mines
        mines = 0  

# Surround each index in lines and append to new list. Insert new line after every 6th index, then print string

minesweeper = []
for row in mine_grid:
    for col in row:
        minesweeper.append("|" + str(col) + "|")

new_line = 6
for i in range(-1, len(minesweeper), new_line):
    minesweeper.insert(i+new_line, "\n")
final_minesweeper = "".join(minesweeper)
print(final_minesweeper)