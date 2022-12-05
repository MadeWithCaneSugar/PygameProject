import pygame, random
import config
from pygame.math import Vector2

# making a class for the player that will be controlled
class PLAYER: 
    def __init__(self) -> None:
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1,0)
        self.new_block = False
    
    def draw_player(self):
        for block in self.body:
            # creating a rectangle
            y_pos = block.y * config.cell_size
            x_pos = block.x * config.cell_size
            block_rect = pygame.Rect(x_pos, y_pos, config.cell_size, config.cell_size)
            # drawing a rectangle
            pygame.draw.rect(config.screen, (0,0,255), block_rect)

    def player_target(self, dx, dy):
        if self.body[0][0] > dx:
            self.direction = Vector2(-1, 0)
        if self.body[0][0] < dx:
            self.direction = Vector2(1, 0)
        if self.body[0][1] > dy:
            self.direction = Vector2(0, -1)
        if self.body[0][1] < dy:
            self.direction = Vector2(0, 1)

    def player_demo(self):
        self.player_target(self.point.pos[0], self.point.pos[1])

    def move(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True