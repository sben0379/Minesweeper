# Minesweeper
## Summary
This is an ongoing project to recreate the classic game Minesweeper using Python. The programme uses a 2D list to simulate a minefield grid and randomly populate it with mines and empty squares. The programme is able to detect how many mines are adjacent to each empty square and display and integer accordingly. 
## Latest Update
### Version 0.3
* Programme now recognises mouse input
* Game window closes if user clicks on a mine
## Planned Updates 
* Keep cell contents hidden from user
* Reveal contents of cell when user clicks on it
* Add correct functionality when user clicks on an empty cell
## Update history
### Version 0.2.1
* Fixed bug causing infinite loop in minefield display
### Version 0.2
* The minefield is now represented graphically 
### Version 0.1
* Generates an empty 5x5 grid and then randomly replaces each index with either a mine (#) or an empty space (-)
* Checks each empty grid space to count how many ajacent spaces are occupied by a mine and replaces - with an integer accordlingly
