import pygame
from components import player, computer, point

class MAIN:
    def __init__(self) -> None:
        self.player = player.PLAYER()
        self.computer = computer.COMPUTER()
        self.point = point.POINT()

    def update(self):
        self.player.move()
        self.computer.move()

    def draw_elements(self):
        self.point.draw_point()
        self.player.draw_player()
        self.computer.draw_computer()