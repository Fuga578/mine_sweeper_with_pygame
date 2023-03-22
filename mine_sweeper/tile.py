import pygame

class Tile:

    def __init__(self, position, image):

        self.position = position
        self.image = image
        self.rect = self.image.get_rect(topleft = self.position)

        self.bomb = False
        self.neighbor_bomb_num = 0

        self.open = False
        self.check = False