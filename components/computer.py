import pygame, random, config
from pygame.math import Vector2
from components import player

# Not implemented. Ran out of time. Un-Commenting the computer code calls
# in update in main.py will bring up a computer controlled opponent that will target
# points and move towards them. The algorithm is a direct path that ignores any
# obstacles, so it dies pretty quickly as the snakes get longer, but I know of some ways
# to change this(though I haven't implemented them)

# I plan on implementing this further in the future because I've been really enjoying
# this project, but alas right now I don't have time.

class COMPUTER:
    def __init__(self) -> None:
        self.body = [Vector2(10, 11), Vector2(11, 11), Vector2(12, 11)]
        self.direction = Vector2(-1,0)
        self.new_block = False
    
    def draw_computer(self):
        for block in self.body:
            y_pos = block.y * config.cell_size
            x_pos = block.x * config.cell_size
            block_rect = pygame.Rect(x_pos, y_pos, config.cell_size, config.cell_size)
            pygame.draw.rect(config.screen, (255,0,0), block_rect)

    def computer_target(self, dx, dy):
        if self.body[0][0] > dx:
            self.direction = Vector2(-1, 0)
        if self.body[0][0] < dx:
            self.direction = Vector2(1, 0)
        if self.body[0][1] > dy:
            self.direction = Vector2(0, -1)
        if self.body[0][1] < dy:
            self.direction = Vector2(0, 1)

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