import pygame, sys, settings, level, player, entity

class Director:
    def __init__(self):
        """
        Director is responsible for all game mechanics
        """
        self.level = level.Level("level1.txt")
        self.player = player.Player(100,100)
    
    def checkEvents(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    self.player.jump()

    
    def update(self, dt):
        self.checkEvents()
        entity.entities.update(dt, self.level.tiles)
    
    def draw(self, surface):
        self.level.draw(surface)
        entity.entities.draw(surface)