import pygame

# цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREY = (200, 200, 200)

class Wall:
    def __init__(self, grid_size):
        self.pos = (0, 0)
        self.x, self.y = self.pos 
        self.width = grid_size[0]
        self.height = grid_size[1]
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(GREY)  # Залить стену белым цветом

    def update(self):
        self.rect.topleft = (int(self.x), int(self.y))

    def draw(self, virtual_surface):
        virtual_surface.blit(self.image, self.rect)


class Grid:
    def __init__(self, width, height, grid_size, map_width, map_height):
        self.tile_width = grid_size[0]
        self.tile_height = grid_size[1]
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.rect = pygame.Rect(self.x, self.y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)

        for y in range(map_height):
            for x in range(map_width):
                pygame.draw.rect(
                    self.image,
                    WHITE,
                    (x * self.tile_width, y * self.tile_height, self.tile_width, self.tile_height),
                    1
                )

    def update(self):
        self.rect.topleft = (int(self.x), int(self.y))

    def draw(self, virtual_surface):
        virtual_surface.blit(self.image, (self.x, self.y))


class Player:
    def __init__(self, grid_size):
        self.width = grid_size[0]
        self.height = grid_size[1]
        self.x = 0
        self.y = 0
        self.pos = (self.x, self.y)
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.image.fill(WHITE)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, events, grid_size):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.y -= grid_size[1]
                elif event.key == pygame.K_DOWN:
                    self.y += grid_size[1]
                elif event.key == pygame.K_LEFT:
                    self.x -= grid_size[0]
                elif event.key == pygame.K_RIGHT:
                    self.x += grid_size[0]

        self.rect.topleft = (int(self.x), int(self.y))

    def draw(self, virtual_surface):
        virtual_surface.blit(self.image, self.rect)