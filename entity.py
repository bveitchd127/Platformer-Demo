import pygame, settings

entityGravity = 1500
entities = pygame.sprite.Group()

class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        entities.add(self)
        self.image = pygame.Surface( (3*settings.tileSize//4, 3*settings.tileSize//4) )
        self.rect = self.image.get_rect(topleft = (x, y))

        self.velocity = pygame.math.Vector2()
        self.resetCollisions()
    
    def resetCollisions(self):
        self.collisions = {
            "top": False,
            "right": False,
            "bottom": False,
            "left": False
        }
    
    def verticalMovement(self, dt, tiles):
        self.velocity.y += entityGravity * dt
        self.rect.y += self.velocity.y * dt

        for tile in tiles:
            if tile.rect.colliderect(self.rect):
                if self.velocity.y > 0:
                    self.collisions["bottom"] = True
                    self.rect.bottom = tile.rect.top
                    self.velocity.y = 10
                elif self.velocity.y < 0:
                    self.collisions["top"] = True
                    self.rect.top = tile.rect.bottom
                    self.velocity.y = 0
    
    def horizontalMovement(self, dt, tiles):
        self.rect.x += self.velocity.x * dt
        for tile in tiles:
            if tile.rect.colliderect( self.rect ):
                if self.velocity.x > 0:
                    self.collisions["right"] = True
                    self.rect.right = tile.rect.left
                elif self.velocity.x < 0:
                    self.collisions["left"] = True
                    self.rect.left = tile.rect.right

    
    def update(self, dt, tiles):
        self.resetCollisions()
        self.horizontalMovement(dt, tiles)
        self.verticalMovement(dt, tiles)
    
    def draw(self, surface):
        pygame.draw.rect(surface, "red", self.rect, 1)
        surface.blit(self.image, self.rect)

        