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
        self.jumpSound = pygame.mixer.Sound("assets/sfx/jump.wav")
        
        self.health = 10
    
    def jump(self):
        if self.jumpCount > 0:
            self.jumpSound.play()
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
                e.velocity.y -= 200
                if self.facingLeft:
                    e.velocity.x -= 400
                else:
                    e.velocity.x += 400

    def heavyAttack(self):
        print("I'm heavy attacking!")
    
    def checkForStar(self):
        for star in self.director.stars:
            if star.rect.colliderect(self.rect):
                self.health = 10
                self.healthRect.width = 48
                star.kill()

    def damage(self, amountOfDamage):
        self.health -= amountOfDamage
        self.healthRect.width = 48 * (self.health/10)
        if self.health <= 0:
            spawnPoint = self.director.getPlayerSpawn()
            self.rect.center = spawnPoint
            self.velocity = pygame.math.Vector2()
            self.health = 10
            self.healthRect.width = 48
    
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
        self.checkForStar()

        super().update(dt, tiles)
    
    def draw(self, surface):
        # punchHitbox = pygame.Rect(self.rect.topleft + self.director.offset, (96,64))
        
        # if self.facingLeft:
        #     punchHitbox.midright = self.rect.center + self.director.offset
        # else:
        #     punchHitbox.midleft = self.rect.center + self.director.offset
        # pygame.draw.rect(surface, "red", punchHitbox, 1)
        self.healthBarRect.midbottom = self.rect.midtop + self.director.offset
        pygame.draw.rect(surface, "black", self.healthBarRect, 0, 2)
        self.healthRect.topleft = self.healthBarRect.topleft
        pygame.draw.rect(surface, "green", self.healthRect   , 0, 2)
        super().draw(surface)
    
    
