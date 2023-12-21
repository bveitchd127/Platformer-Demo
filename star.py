import pygame, entity

class Star(entity.Entity):
    def __init__(self, director, x, y):
        super().__init__(director, x, y)
        # 48, 48

        # pygame.image.load($filename$)
        starCoords = [(24,0),(30,18),(48,18),(35,28),(42,48),(24,36),(6,48),(13,28),(0,18),(18,18)]
        pygame.draw.polygon(self.image, (186, 152,  77), starCoords)
        pygame.draw.polygon(self.image, (100,  73,  44), starCoords, 3)