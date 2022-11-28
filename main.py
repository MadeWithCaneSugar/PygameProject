import pygame, sys, random
from pygame.math import Vector2

# Classes #########################################################################################

# making a class for points to be eaten. Will be moved into seperate file later
class POINT:
    def __init__(self) -> None:
        # creating an x and y position
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_point(self):
        # create a rectangle
        x_pos = self.pos.x * cell_size
        y_pos = self.pos.y * cell_size
        point_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
        # draw a rectangle
        pygame.draw.rect(screen, (255, 0, 0), point_rect)

# making a class for the player that will be controlled
class PLAYER: 
    def __init__(self) -> None:
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1,0)
    
    def draw_player(self):
        for block in self.body:
            # creating a rectangle
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            # drawing a rectangle
            pygame.draw.rect(screen, (0,0,255), block_rect)

    def move(self):
        body_copy = self.body[:]
        # removing the -1 in the above line is the one thing between snake and Tron 
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    # code for colliding with walls and ribbons, your own or otherwise
    def collision(self):
        pass

class COMPUTER:
    def __init__(self) -> None:
        pass

    def draw_computer(self):
        pass

###################################################################################################

pygame.init()
cell_size = 10
cell_number = 100
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

# have to initialize this as a variable. Idk why, but it won't display properly if you don't
point = POINT()
player = PLAYER()

# updating the screen at a set time intervals in ms
screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update, 150)

# Mainloop ########################################################################################

while True:
    # event for closing the window when hitting the close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # triggering player movement when the screen updates
        if event.type == screen_update:
            player.move()

        # keyboard inputs
        # 2nd nested if statement is to stop perfect 180s
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if player.direction == Vector2(0, 1):
                    pass
                else:
                    player.direction = Vector2(0, -1)

            if event.key == pygame.K_DOWN:
                if player.direction == Vector2(0, -1):
                    pass
                else:
                    player.direction = Vector2(0, 1)

            if event.key == pygame.K_LEFT:
                if player.direction == Vector2(1, 0):
                    pass
                else:
                    player.direction = Vector2(-1, 0)

            if event.key == pygame.K_RIGHT:
                if player.direction == Vector2(-1, 0):
                    pass
                else:
                    player.direction = Vector2(1, 0)

    # changing the background screen color
    screen.fill((175,215,70))

    # drawing the point using the variable I assigned outside of the loop
    point.draw_point()
    player.draw_player()

    # drawing elements
    pygame.display.update()

    # capping framerate
    # no minimum framerate because this game is going to be relatively light and simple
    clock.tick(60)