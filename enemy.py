import pygame, random, entity, animation

class Enemy(entity.Entity):
    def __init__(self, director, x, y):
        super().__init__(director, x, y)
        self.animStatus = "idle"
        self.animDict = {
            "idle": animation.Animation("assets/gfx/idle.png", 12, (0,8)),
            "run" : animation.Animation("assets/gfx/run.png" , 12, (0,8)),
            "jump": animation.Animation("assets/gfx/jump.png",  4, (0,8)),
        }
        self.movementSpeed = 300
        
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
    
    def updateMovement(self):
        playerPos = pygame.math.Vector2(self.director.player.rect.center)
        myPos = pygame.math.Vector2(self.rect.center)
        eToP = playerPos - myPos
        if 50 < eToP.magnitude() < 300:
            # eToP.normalize() would achieve the same thing
            eToP.scale_to_length(1)
            self.direction = eToP
        else:
            self.direction = pygame.math.Vector2()

    def update(self, dt, tiles):
        self.updateMovement()
        
        self.updateAnimation(dt)

        super().update(dt, tiles)