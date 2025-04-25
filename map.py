import pygame
from object import Wall, Player  # Add Player to the import list

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

# количесто ячеек по горизонтали и вертикали
map_width = len(map[0])
map_height = len(map)

print("map_width", map_width)
print("map_height", map_height)

def initialize_map(grid, grid_size):
    global map_initialized, walls, players

    for y, row in enumerate(map):
        for x, tile in enumerate(row):
            if tile == 1:
                wall = Wall(grid_size)  # Убираем позицию (x, y)
                wall.x = x * grid.tile_width
                wall.y = y * grid.tile_height
                walls.append(wall)
            
            if tile == "P":
                player = Player(grid_size)
                player.x = x * grid.tile_width
                player.y = y * grid.tile_height
                player.pos = (player.x, player.y)
                players.append(player)