import pygame, random, config
from pygame.math import Vector2
from components import player

class COMPUTER:
    def __init__(self) -> None:
        self.body = [Vector2(5, 11), Vector2(6, 11), Vector2(7, 11)]
        self.direction = Vector2(1,0)
    
    def draw_computer(self):
        for block in self.body:
            # creating a rectangle
            y_pos = block.y * config.cell_size
            x_pos = block.x * config.cell_size
            block_rect = pygame.Rect(x_pos, y_pos, config.cell_size, config.cell_size)
            # drawing a rectangle
            pygame.draw.rect(config.screen, (255,0,0), block_rect)

    def move(self):
        body_copy = self.body[:-1]
        # removing the -1 in the above line is the one thing between snake and Tron 
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def computer_target(self):
        # should be used for computer algorithm
        pass
