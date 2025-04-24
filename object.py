import pygame

class Wall:
    def __init__(self, pos, width = 66, height = 100):
        self.x, self.y = pos
        self.width = width
        self.height = height
        self.x, self.y = pos
        self.rect = pygame.Rect(self.x, self.y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)  # Прозрачный фон

        # Нарисовать только границу
        pygame.draw.rect(self.image, (255, 0, 0), (0, 0, width, height), 1)

    def update(self):
        self.rect.topleft = (self.x, self.y)

    def draw(self, virtual_surface):
        virtual_surface.blit(self.image, self.rect)


class Grid:
    def __init__(self, width, height, tile_width=66, tile_height=100):
        self.width = width
        self.height = height
        self.tile_width = tile_width
        self.tile_height = tile_height

    def draw(self, virtual_surface):
        # Рисуем вертикальные линии
        x = 0
        while x < self.width:
            pygame.draw.line(virtual_surface, (255, 255, 255), (x, 0), (x, self.height))
            x += self.tile_width
        
        # Рисуем горизонтальные линии
        y = 0
        while y < self.height:
            pygame.draw.line(virtual_surface, (255, 255, 255), (0, y), (self.width, y))
            y += self.tile_height


class Player:
    def __init__(self, grid):
        self.width = 66
        self.height = 100
        self.x = 0
        self.y = 0
        self.pos = (self.x, self.y)
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.image.fill((255, 255, 255))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.grid = grid  # Store the Grid instance

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.y -= self.grid.tile_height
                elif event.key == pygame.K_DOWN:
                    self.y += self.grid.tile_height
                elif event.key == pygame.K_LEFT:
                    self.x -= self.grid.tile_width
                elif event.key == pygame.K_RIGHT:
                    self.x += self.grid.tile_width

        self.rect.topleft = (self.x, self.y)

    def draw(self, virtual_surface):
        virtual_surface.blit(self.image, self.rect)