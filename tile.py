import pygame, settings

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface( (settings.tileSize,settings.tileSize) )
        self.rect = self.image.get_rect(topleft = (x, y))
        self.image.fill( settings.tileColor )
