import pygame, entity, animation, random

class Enemy(entity.Entity):
    def __init__(self, director, x, y):
        super().__init__(director, x, y)
        self.animStatus = "idle"
        self.animDict = {
            "idle": animation.Animation("assets/gfx/idle.png", 12, (0,8)),
            "run" : animation.Animation("assets/gfx/run.png" , 12, (0,8)),
            "jump": animation.Animation("assets/gfx/jump.png",  4, (0,8)),
        }
        self.movementSpeed = random.randint(150,200)
        self.health = 5

        self.attackSpeed = 2
        self.attackCooldown = random.random()*2
        self.projectileSpeed = 500
    
    def damage(self, amountOfDamage):
        self.health -= amountOfDamage
        self.healthRect.width = 48 * (self.health/5)
        if self.health <= 0:
            self.kill()

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
        playerPos  = pygame.math.Vector2(self.director.player.rect.center)
        myPosition = pygame.math.Vector2(self.rect.center)
        enemyToPlayer = playerPos - myPosition

        if 0   < enemyToPlayer.magnitude() < 250:
            enemyToPlayer.scale_to_length(1)
            self.direction = -enemyToPlayer
        elif 250 <= enemyToPlayer.magnitude() <= 350 and self.attackCooldown == 0:
            #attack
            enemyToPlayer.scale_to_length(self.projectileSpeed)
            self.director.spawnProjectile(self.rect.center, enemyToPlayer)
            self.attackCooldown = 2

        elif 350 < enemyToPlayer.magnitude() < 600:
            enemyToPlayer.scale_to_length(1)
            # enemyToPlayer.normalize()
            self.direction = enemyToPlayer

        else:
            self.direction = pygame.math.Vector2(0,0)

    def update(self, dt, tiles):      
        if self.attackCooldown > 0:
            self.attackCooldown -= dt  
        else:
            self.attackCooldown = 0
        self.updateAnimation(dt)
        self.updateMovement()
        super().update(dt, tiles)
    
    def draw(self, surface):
        self.healthBarRect.midbottom = self.rect.midtop + self.director.offset
        pygame.draw.rect(surface, "black", self.healthBarRect, 0, 2)
        self.healthRect.topleft = self.healthBarRect.topleft
        pygame.draw.rect(surface, "green", self.healthRect   , 0, 2)
        super().draw(surface)