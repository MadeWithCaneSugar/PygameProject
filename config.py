import pygame

# this is the config file that defines many of the fundamental values used in the game

# determines the size of the playfield as well as how many divisions it's made of
cell_size = 20
cell_number = 40

# some initialization applying the size
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

# setting how quickly the screen updates in ms (lower number means faster updates)
max_speed = 50

# maximum frame rate of the game.
# no easily implemented minimum unfortunately
max_frames = clock.tick(60)