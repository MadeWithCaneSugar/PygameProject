import pygame, random, config
from pygame.math import Vector2

# making a class for the player that will be controlled
class PLAYER: 
    def __init__(self) -> None:
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1,0)
    
    def draw_player(self):
        for block in self.body:
            # creating a rectangle
            y_pos = block.y * config.cell_size
            x_pos = block.x * config.cell_size
            block_rect = pygame.Rect(x_pos, y_pos, config.cell_size, config.cell_size)
            # drawing a rectangle
            pygame.draw.rect(config.screen, (0,0,255), block_rect)

    def move(self):
        body_copy = self.body[:-1]
        # removing the -1 in the above line is the one thing between snake and Tron 
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    # code for colliding with walls and ribbons, your own or otherwise
    def collision(self):
        pass