import pygame
from object import *

map = False
map_initialized = False

walls = []  # Список для хранения всех стен
players = []  # Список для хранения всех игроков

map = [
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  "P",  1,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
]

def initialize_map(grid):
    global map_initialized, walls, players

    for y, row in enumerate(map):
        for x, tile in enumerate(row):
            if tile == 1:
                wall = Wall((x * grid.tile_width, y * grid.tile_height))
                walls.append(wall)

            if tile == "P":
                player = Player(grid)  # Pass the Grid instance
                player.x = x * grid.tile_width
                player.y = y * grid.tile_height
                player.pos = (player.x, player.y)
                players.append(player)