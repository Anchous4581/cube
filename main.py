import pygame
from object import *
from map import *

pygame.init()

info = pygame.display.Info()
clock = pygame.time.Clock()

screen_resolutions = [
    (800, 600),
    (1024, 768),
    (1280, 720),
    (1366, 768),
    (1440, 900),
    (1600, 900),
    (1920, 1080),
    (2560, 1440),
]

screen_resolution_index = 0
current_resolution = screen_resolutions[screen_resolution_index]

is_fullscreen = False
flags = pygame.RESIZABLE

screen = pygame.display.set_mode(current_resolution, flags)
virtual_surface = pygame.Surface(current_resolution)

pygame.display.set_caption("CUBE")

# цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

grid = Grid(800, 600)

initialize_map(grid)

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            elif event.key == pygame.K_1:
                is_fullscreen = not is_fullscreen
                if is_fullscreen:
                    flags = pygame.FULLSCREEN
                else:
                    flags = pygame.RESIZABLE
                screen = pygame.display.set_mode(current_resolution, flags)
                virtual_surface = pygame.Surface(current_resolution)

            elif event.key == pygame.K_2:
                screen_resolution_index = (screen_resolution_index + 1) % len(screen_resolutions)
                current_resolution = screen_resolutions[screen_resolution_index]
                screen = pygame.display.set_mode(current_resolution, flags)
                virtual_surface = pygame.Surface(current_resolution)

    # Очистка виртуального экрана
    virtual_surface.fill((0, 0, 0))

    # Рисуем сетку
    grid.draw(virtual_surface)

    # Обновление и отрисовка всех стен
    for wall in walls:
        wall.update()
        wall.draw(virtual_surface)

    # Обновление и отрисовка всех игроков
    for player in players:
        player.update(events)  # Передаем список событий
        player.draw(virtual_surface)

    # Отрисовка
    scaled_surface = pygame.transform.scale(virtual_surface, screen.get_size())
    screen.blit(scaled_surface, (0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()