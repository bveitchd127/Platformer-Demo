import pygame, settings, entity

class Player(entity.Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        #self.image.fill(settings.playerColor)
        self.texture = pygame.image.load("assets/gfx/idle.png")
        self.image.blit(self.texture, (0,0))
        self.movementSpeed = 400
        self.jumpCount = 2
    
    def jump(self):
        if self.jumpCount > 0:
            self.jumpCount -= 1
            self.velocity.y = -800
    
    def getInput(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.velocity.x = -self.movementSpeed
        elif keys[pygame.K_d]:
            self.velocity.x = self.movementSpeed
        else:
            self.velocity.x = 0
    
    def update(self, dt, tiles):
        self.getInput()
        if self.collisions["bottom"] and self.velocity.y > 0:
            self.jumpCount = 2
        super().update(dt, tiles)
    
