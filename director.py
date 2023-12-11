import pygame, sys, settings, level, player, entity, enemy, random, projectile

class Director:
    def __init__(self):
        """
        Director is responsible for all game mechanics
        """
        self.player = player.Player(self, 100,100)
        self.enemies = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.level = level.Level(self, "level1.txt")
        self.offset = (settings.screenWidth//2, settings.screenHeight//2) - pygame.math.Vector2(self.player.rect.center)
        
    def spawnEnemy(self, x, y):
        self.enemies.add( enemy.Enemy(self,x,y) )
    
    def spawnProjectile(self, position, velocity):
        self.projectiles.add(projectile.Projectile(self, position[0], position[1], velocity))

    def checkEvents(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    self.player.jump()
                if e.key == pygame.K_RIGHT:
                    self.player.velocity.x = 1000
                    self.player.velocity.y = -300
                if e.key == pygame.K_LEFT:
                    self.player.velocity.x = -1000
                    self.player.velocity.y = -300
                if e.key == pygame.K_e:
                    x = random.randint(70,1150)
                    y = random.randint(70,650)
                    self.spawnEnemy(x,y)
                
                if e.key == pygame.K_1:
                    self.enemies.empty()
                    self.level = level.Level(self, "level1.txt")
                    
                if e.key == pygame.K_2:
                    self.enemies.empty()
                    self.level = level.Level(self, "level2.txt")

    def updateOffset(self, dt):
        self.offset += settings.cameraSpeed*((640,360) - self.offset - self.player.rect.center)*dt
        self.offset.y = pygame.math.clamp(self.offset.y, -128, 4000)
    
    def checkForFallenPlayer(self):
        if self.player.rect.y > 4000:
            self.player.rect.topleft = (400,100)
            self.player.velocity = pygame.math.Vector2()

    def update(self, dt):
        self.checkEvents()
        self.checkForFallenPlayer()
        self.updateOffset(dt)
        
        self.player.update(dt, self.level.tiles)
        self.enemies.update(dt, self.level.tiles)
        self.projectiles.update(dt, self.level.tiles)
    
    def draw(self, surface):
        self.level.draw(surface)
        
        self.player.draw(surface)
        for e in self.enemies:
            e.draw(surface)
        for p in self.projectiles:
            p.draw(surface)