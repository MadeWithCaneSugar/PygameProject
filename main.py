import pygame, sys, random, config
from pygame.math import Vector2
from components import point, player, computer

pygame.init()
cell_size = config.cell_size
cell_number = config.cell_number
screen = config.screen
clock = config.clock

# have to initialize this as a variable. Idk why, but it won't display properly if you don't
point = point.POINT()
player = player.PLAYER()
computer = computer.COMPUTER()

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
    screen.fill((0,0,0))

    # drawing the point using the variable I assigned outside of the loop
    point.draw_point()
    player.draw_player()
    computer.draw_computer()

    # drawing elements
    pygame.display.update()

    # capping framerate
    # no minimum framerate because this game is going to be relatively light and simple
    clock.tick(config.max_frames)