import pygame, sys, random, config
import main
from pygame.math import Vector2
from components import point, player, computer

pygame.init()
cell_size = config.cell_size
cell_number = config.cell_number
screen = config.screen
clock = config.clock

# I didn't use your starter code because I got a bit overwhelmed by it, so I started from scratch
# admittedly this means I never implemented the code for multiple screens. Unfortunately 

# updating the screen at a set time intervals in ms
screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update, config.max_speed)

# Mainloop ########################################################################################

main_game = main.MAIN()

while True:
    # event for closing the window when hitting the close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # triggering player movement when the screen updates
        if event.type == screen_update:
            main_game.update()

        # keyboard inputs
        # 2nd nested if statement is to stop perfect 180s
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if main_game.player.direction == Vector2(0, 1):
                    pass
                else:
                    main_game.player.direction = Vector2(0, -1)

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if main_game.player.direction == Vector2(0, -1):
                    pass
                else:
                    main_game.player.direction = Vector2(0, 1)

            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if main_game.player.direction == Vector2(1, 0):
                    pass
                else:
                    main_game.player.direction = Vector2(-1, 0)

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if main_game.player.direction == Vector2(-1, 0):
                    pass
                else:
                    main_game.player.direction = Vector2(1, 0)

    # changing the background screen color
    screen.fill((255,255,255))

    main_game.draw_elements()

    # drawing elements
    pygame.display.update()

    # capping framerate
    # no minimum framerate because this game is going to be relatively light and simple
    clock.tick(config.max_frames)