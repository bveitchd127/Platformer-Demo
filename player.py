import pygame, settings, entity, animation

class Player(entity.Entity):
    def __init__(self, director, x, y):
        super().__init__(director, x, y)

        self.animStatus = "idle"
        self.animDict = {
            "idle": animation.Animation("assets/gfx/idle.png", 12, (0,8)),
            "run" : animation.Animation("assets/gfx/run.png" , 12, (0,8)),
            "jump": animation.Animation("assets/gfx/jump.png",  4, (0,8)),
        }
        self.movementSpeed = 400
        self.jumpCount = 2
        # player width is about 14, 29
        #self.rect = pygame.Rect(x, y, 14, 29)
    
    def jump(self):
        if self.jumpCount > 0:
            self.jumpCount -= 1
            self.velocity.y = -800
    

    def lightAttack(self):
        punchHitbox = pygame.Rect(self.rect.topleft, (96,64))
        
        if self.facingLeft:
            punchHitbox.midright = self.rect.center
        else:
            punchHitbox.midleft = self.rect.center
        for e in self.director.enemies:
            if e.rect.colliderect(punchHitbox):
                e.damage(1)

    def heavyAttack(self):
        print("I'm heavy attacking!")
    

    def damage(self, amountOfDamage):
        print("OW I took " + str(amountOfDamage) + " damage!")
    
    def getInput(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0
    
    def updateAnimStatus(self):
        if self.collisions["bottom"]:
            if self.direction.x != 0:
                self.animStatus = "run"
            else:
                self.animStatus = "idle"
        else:
            self.animStatus = "jump"

    def updateAnimation(self, dt):
        self.updateDirection()
        self.updateAnimStatus()
        
        self.image = self.animDict[self.animStatus].getFrame()
        if self.facingLeft:
            self.image = pygame.transform.flip(self.image, True, False)

        self.animDict[self.animStatus].update(dt)

    def update(self, dt, tiles):
        self.getInput()
        if self.collisions["bottom"] and self.velocity.y > 0:
            self.jumpCount = 2
        
        self.updateAnimation(dt)

        super().update(dt, tiles)
    
    def draw(self, surface):
        punchHitbox = pygame.Rect(self.rect.topleft + self.director.offset, (96,64))
        
        if self.facingLeft:
            punchHitbox.midright = self.rect.center + self.director.offset
        else:
            punchHitbox.midleft = self.rect.center + self.director.offset
        pygame.draw.rect(surface, "red", punchHitbox, 1)
        super().draw(surface)
    
    
