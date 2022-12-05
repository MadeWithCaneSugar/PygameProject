import pygame, random
import config
from pygame.math import Vector2

screen = config.screen

# making a class for the player that will be controlled
class PLAYER: 
    def __init__(self) -> None:
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1,0)
        self.new_block = False

        # NOT DOING CORNERS, NO GODDAMN TIME
        self.snake_head_right = config.snake_head_sprite
        self.snake_head_left = pygame.transform.rotate(config.snake_head_sprite, 180)
        self.snake_head_up = pygame.transform.rotate(config.snake_head_sprite, 90)
        self.snake_head_down = pygame.transform.rotate(config.snake_head_sprite, 270)
        
        self.snake_body_horizontal = config.snake_body_sprite
        self.snake_body_vertical = pygame.transform.rotate(config.snake_body_sprite, 90)
        
        self.snake_butt_right = config.snake_butt_sprite
        self.snake_butt_left = pygame.transform.rotate(config.snake_butt_sprite, 180)
        self.snake_butt_up = pygame.transform.rotate(config.snake_butt_sprite, 90)
        self.snake_butt_down = pygame.transform.rotate(config.snake_butt_sprite, 270)
    
    def draw_player(self):
        self.update_head_graphics()
        self.update_butt_graphics()

        for index, block in enumerate(self.body):
            y_pos = block.y * config.cell_size
            x_pos = block.x * config.cell_size
            block_rect = pygame.Rect(x_pos, y_pos, config.cell_size, config.cell_size)
            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.butt, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.snake_body_vertical, block_rect)
                if previous_block.y == next_block.y:
                    screen.blit(self.snake_body_horizontal, block_rect)

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

    # doing some math to determine the relationship between the head
    # and the body chunk right behind it
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0):
            self.head = self.snake_head_left
        elif head_relation == Vector2(-1,0):
            self.head = self.snake_head_right
        elif head_relation == Vector2(0,1):
            self.head = self.snake_head_up
        elif head_relation == Vector2(0,-1):
            self.head = self.snake_head_down

    def update_butt_graphics(self):
        butt_relation = self.body[-1] - self.body[-2]
        if butt_relation == Vector2(1,0):
            self.butt = self.snake_butt_left
        elif butt_relation == Vector2(-1,0):
            self.butt = self.snake_butt_right
        elif butt_relation == Vector2(0,1):
            self.butt = self.snake_butt_up
        elif butt_relation == Vector2(0,-1):
            self.butt = self.snake_butt_down
            
    def update_body_graphics(self):
        body_relation = self.body[1] - self.body[-2]
        if body_relation == Vector2(1,0):
            self.body = self.snake_body_left
        elif body_relation == Vector2(-1,0):
            self.body = self.snake_body_right
        elif body_relation == Vector2(0,1):
            self.body = self.snake_body_up
        elif body_relation == Vector2(0,-1):
            self.body = self.snake_body_down