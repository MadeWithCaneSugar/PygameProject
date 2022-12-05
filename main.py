import pygame, sys, config
from components import player, computer, point

cell_size = config.cell_size
cell_number = config.cell_number

class MAIN:
    def __init__(self) -> None:
        self.player = player.PLAYER()
        self.computer = computer.COMPUTER()
        self.point = point.POINT()

        self.add_block = False

    def update(self):
        self.player.move()
        # self.computer.move()
        self.check_player_collision()
        self.check_fail()
        # self.check_computer_collision()
        # self.computer.computer_target(self.point.pos[0], self.point.pos[1])

    def draw_elements(self):
        self.point.draw_point()
        self.player.draw_player()
        # self.computer.draw_computer()

    def move(self):
        if self.add_block == True:
            body_copy = self.body[:]
            # removing the -1 in the above line is the one thing between snake and Tron 
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

        else:
            body_copy = self.body[:-1]
            # removing the -1 in the above line is the one thing between snake and Tron 
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def check_player_collision(self):
        if self.point.pos == self.player.body[0]:
            print("player point")
            self.point.randomize()
            self.player.add_block()

    def check_computer_collision(self):
        if  self.point.pos == self.computer.body[0]:
            print("computer point")
            self.point.randomize
            self.computer.add_block

    def check_fail(self):
        # checking if the snake strikes a wall
        if (not 0 <= self.player.body[0].x <= cell_number) or (not 0 <= self.player.body[0].y <= cell_number):
            self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()