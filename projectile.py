import pygame, settings

class Projectile(pygame.sprite.Sprite):
    def __init__(self, director, x, y, velocity):
        super().__init__()
        self.director = director
        self.velocity = velocity
        self.image = pygame.Surface(12,12)
        pygame.draw.circle(self.image, "purple", (6,6), 6)
        self.rect = self.image.get_rect(center = (x,y))
    
    def updateMovement(self, dt, tiles):
        self.rect += self.velocity * dt
        
        if self.director.player.rect.colliderect(self.rect):
            self.director.player.damage(1)
            self.kill()

        for tile in tiles:
            if tile.rect.colliderect(self.rect):
                self.kill()

    def update(self, dt, tiles):
        self.updateMovement(dt, tiles)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft + self.director.offset)

        