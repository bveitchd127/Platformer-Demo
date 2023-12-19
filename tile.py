import pygame, settings

def createTileImage(tileSetImage, x, y):
    tileImage = pygame.Surface((32,32))
    tileImage.blit(tileSetImage, (0,0), pygame.Rect(32*x, 32*y, 32, 32))
    tileImage = pygame.transform.scale(tileImage, (settings.tileSize, settings.tileSize))
    tileImage.set_colorkey("black")
    return tileImage


tileSetImage = pygame.image.load("assets/gfx/TX Tileset Ground.png")

tileDict = {
    "X" : createTileImage(tileSetImage, 1, 0),
    "B" : createTileImage(tileSetImage, 1, 1),
    "W" : createTileImage(tileSetImage, 0, 9),
    "C" : createTileImage(tileSetImage, 0, 8),
    "J" : createTileImage(tileSetImage, 4, 7),

    "D" : createTileImage(tileSetImage, 0, 12),
    "F" : createTileImage(tileSetImage, 1, 12),
    "G" : createTileImage(tileSetImage, 2, 12),

    "V": createTileImage(tileSetImage, 15, 3),
    "Z": createTileImage(tileSetImage, 10, 11),
    "T": createTileImage(tileSetImage, 6, 9)
}

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        super().__init__()
        self.type = type
        self.image = pygame.Surface( (settings.tileSize,settings.tileSize) , pygame.SRCALPHA )
        self.rect = self.image.get_rect(topleft = (x, y))
        # self.image.fill( settings.tileColor )
        
        self.image.blit(tileDict[self.type], (0,0))
        