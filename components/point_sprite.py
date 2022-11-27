import pygame
from pygame.math import Vector2
import main

class POINT:
    def __init__(self) -> None:
        # creating an x and y position
        self.x = 5
        self.y = 4
        self.pos = Vector2(self.x, self.y)

    def draw_point(self):
        # create a rectangle
        point_rect = pygame.Rect(self.pos.x, self.pos.y, main.cell_size, main.cell_size)
        # draw a rectangle
        pygame.draw.rect(main.screen, (120, 160, 110), point_rect)