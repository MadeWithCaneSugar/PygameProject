import pygame, random, config
from pygame.math import Vector2

# making a class for points to be eaten.
class POINT:
    def __init__(self) -> None:
        self.randomize()

    def draw_point(self):
        # create a rectangle
        x_pos = self.pos.x * config.cell_size
        y_pos = self.pos.y * config.cell_size
        point_rect = pygame.Rect(x_pos, y_pos, config.cell_size, config.cell_size)
        # draw a rectangle
        pygame.draw.rect(config.screen, (255, 0, 0), point_rect)

    def randomize(self):
        # creating an x and y position
        self.x = random.randint(0, config.cell_number - 1)
        self.y = random.randint(0, config.cell_number - 1)
        self.pos = Vector2(self.x, self.y)