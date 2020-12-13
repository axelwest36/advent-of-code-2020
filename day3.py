import numpy as np

# Part 1
with open("/Users/axelwest/Desktop/Advent of Code/input_day_3.txt", "r+") as file:
    grid = file.readlines()
    x, y = 0, 0
    nr_of_trees = 0
    grid_width = len(grid[0]) - 1 
    
    while y < len(grid):
        if grid[y][x] == '#':
            nr_of_trees = nr_of_trees + 1
        if x >= (grid_width - 3): 
            x = x + 3 - grid_width
        else:
            x = x + 3
        y = y + 1 
    print(nr_of_trees)

# Part 2
with open("/Users/axelwest/Desktop/Advent of Code/input_day_3.txt", "r+") as file:
    grid = file.readlines()
    def traverse_grid(x_step, y_step, grid):
        x, y = 0, 0
        nr_of_trees = 0
        grid_width = len(grid[0]) - 1 
        
        while y < len(grid):
            if grid[y][x] == '#':
                nr_of_trees = nr_of_trees + 1
            if x >= (grid_width - x_step): 
                x = x + x_step - grid_width
            else:
                x = x + x_step
            y = y + y_step
        return nr_of_trees
    combinations = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    results = [traverse_grid(combination[0], combination[1], grid) for combination in combinations]
    print(np.prod(results))