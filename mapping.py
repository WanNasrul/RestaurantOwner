import pygame, sys
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

# game setup
def map():
    bg_surf = pygame.image.load('gameasset/background.png').convert()
    sprite_surf = pygame.image.load('gameasset/tablechair.png').convert_alpha()  # Load sprite with transparency

    TableChairPos = [
        (420, 450),
        (800, 450),
        (770, 300),
    ]

    for pos in TableChairPos:
        bg_surf.blit(sprite_surf, pos)  # Blit the table chair sprite onto the background surface

    return bg_surf