import pygame, settings

entityGravity = 1500
entities = pygame.sprite.Group()

class Entity(pygame.sprite.Sprite):
    def __init__(self, director, x, y):
        super().__init__()
        self.director = director
        entities.add(self)
        self.image = pygame.Surface( (48, 48) )
        self.rect = self.image.get_rect(topleft = (x, y))

        self.velocity = pygame.math.Vector2()
        self.direction = pygame.math.Vector2()
        self.movementSpeed = 100
        self.facingLeft = False
        self.resetCollisions()
    
    def resetCollisions(self):
        self.collisions = {
            "top": False,
            "right": False,
            "bottom": False,
            "left": False
        }
    
    def updateDirection(self):
        if self.direction.x < 0:
            self.facingLeft = True
        elif self.direction.x > 0:
            self.facingLeft = False

    def verticalMovement(self, dt, tiles):
        self.velocity.y += entityGravity * dt
        self.rect.y += self.velocity.y * dt

        self.collisions["top"] = False
        self.collisions["bottom"] = False
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
        xMovement = self.direction.x * self.movementSpeed
        totalXMovement = self.velocity.x + xMovement
        
        if (self.collisions["bottom"]):
            if self.velocity.x > 50:
                self.velocity.x -= 3000*dt
            elif self.velocity.x < -50:
                self.velocity.x += 3000*dt
            else:
                self.velocity.x = 0

        self.rect.x += totalXMovement * dt

        self.collisions["right"] = False
        self.collisions["left"] = False
        for tile in tiles:
            if tile.rect.colliderect( self.rect ):
                if totalXMovement > 0:
                    self.collisions["right"] = True
                    self.rect.right = tile.rect.left
                elif totalXMovement < 0:
                    self.collisions["left"] = True
                    self.rect.left = tile.rect.right

    
    def update(self, dt, tiles):
        self.horizontalMovement(dt, tiles)
        self.verticalMovement(dt, tiles)
    
    def draw(self, surface):
        if settings.hitboxToggle:
            pygame.draw.rect(surface, "red", pygame.Rect(self.rect.topleft + self.director.offset,(self.rect.size)), 1)
        surface.blit(self.image, self.rect.topleft + self.director.offset)

        