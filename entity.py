import pygame, settings

entityGravity = 1500
#entities = pygame.sprite.Group()

class Entity(pygame.sprite.Sprite):
    def __init__(self, director, x, y):
        super().__init__()
        self.director = director
        #entities.add(self)
        self.image = pygame.Surface( (3*settings.tileSize//4, 3*settings.tileSize//4) )
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
        self.velocity.y = pygame.math.clamp(self.velocity.y, -60*settings.tileSize, 60*settings.tileSize)
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
        self.velocity.x = pygame.math.clamp(self.velocity.x, -60*settings.tileSize, 60*settings.tileSize)
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
                    self.velocity.x = 0
                elif totalXMovement < 0:
                    self.collisions["left"] = True
                    self.rect.left = tile.rect.right
                    self.velocity.x = 0

    
    def update(self, dt, tiles):
        #self.resetCollisions()
        self.horizontalMovement(dt, tiles)
        self.verticalMovement(dt, tiles)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft + self.director.offset)

        