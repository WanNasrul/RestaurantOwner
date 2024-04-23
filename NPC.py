import pygame
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement

matrix = [
    [1,1,1,1,1,1],
    [1,0,1,1,1,1],
    [1,1,1,1,1,1]
]

#creating grid
grid = Grid(matrix= matrix)

#start and end cell
start = grid.node(0,0)
end = grid.node(5,2)

#for the movement
finder = AStarFinder(diagonal_movement= DiagonalMovement.always)

path,runs = finder.find_path(start,end,grid)

print(path)
print(runs)