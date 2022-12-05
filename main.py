import pygame, sys, config
from components import player, computer, point

cell_size = config.cell_size
cell_number = config.cell_number
game_font = config.game_font

tile = config.tile_sprite
screen = config.screen

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
        # self.player.player_target(self.point.pos[0], self.point.pos[1])
        self.check_fail()
        # self.check_computer_collision()
        # self.computer.computer_target(self.point.pos[0], self.point.pos[1])

    def draw_elements(self):
        self.draw_tiles()
        self.draw_score()
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

        # checking if the snake strikes itself
        for block in self.player.body[1:]:
            if block  == self.player.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()

    def draw_tiles(self):
        for row in range(cell_number):
            for col in range(cell_number):
                    tile_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                    screen.blit(tile, tile_rect)

    def draw_score(self):
        score_text = str(len(self.player.body) - 3)
        score_surface = game_font.render(score_text, False, (0,0,0))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 60)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        screen.blit(score_surface, score_rect)