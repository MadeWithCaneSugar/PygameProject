import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400,500))
clock = pygame.time.Clock()

while True:
    # event for closing the window when hitting the close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # changing the background screen color
    screen.fill((175,215,70))

    # drawing elements
    pygame.display.update()

    # capping framerate
    # no minimum framerate because this game is going to be relatively light and simple
    clock.tick(60)