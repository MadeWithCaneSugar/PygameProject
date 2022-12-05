import pygame

# this is the config file that defines many of the fundamental values used in the game

# determines the size of the playfield as well as how many divisions it's made of
cell_size = 40
cell_number = 20

# some initialization applying the size
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

# font
pygame.font.init()
game_font = pygame.font.Font("./graphics/PAPYRUS.ttf", 25)

# setting how quickly the screen updates in ms (lower number means faster updates)
max_speed = 150

# maximum frame rate of the game.
# no easily implemented minimum unfortunately
max_frames = clock.tick(30)

# sprites
point_sprite = pygame.transform.scale(pygame.image.load("./graphics/point.png").convert_alpha(), (cell_size, cell_size))
snake_head_sprite = pygame.transform.scale(pygame.image.load("./graphics/snake_head.png").convert_alpha(), (cell_size, cell_size))
snake_body_sprite = pygame.transform.scale(pygame.image.load("./graphics/snake_body.png").convert_alpha(), (cell_size, cell_size))
snake_butt_sprite = pygame.transform.scale(pygame.image.load("./graphics/snake_butt.png").convert_alpha(), (cell_size, cell_size))
tile_sprite = pygame.transform.scale(pygame.image.load("./graphics/square.png").convert_alpha(), (cell_size, cell_size))