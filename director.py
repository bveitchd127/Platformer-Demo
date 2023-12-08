import pygame, sys, settings, level, player, entity, enemy, random

class Director:
    def __init__(self):
        """
        Director is responsible for all game mechanics
        """
        self.player = player.Player(self, 100,100)
        self.enemies = pygame.sprite.Group()
        self.level = level.Level(self, "level1.txt")
        print(self.player.rect.center)
        self.offset = (settings.screenWidth//2, settings.screenHeight//2) - pygame.math.Vector2(self.player.rect.center)
    
    def spawnEnemy(self, x, y):
        self.enemies.add( enemy.Enemy(self,x,y) )


    def checkEvents(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    self.player.jump()
                if e.key == pygame.K_h:
                    settings.hitboxToggle = not settings.hitboxToggle
                if e.key == pygame.K_RIGHT:
                    self.player.velocity.x = 1000
                    self.player.velocity.y = -300
                if e.key == pygame.K_LEFT:
                    self.player.velocity.x = -1000
                    self.player.velocity.y = -300
                if e.key == pygame.K_e:
                    x = random.randint(64+8, settings.screenWidth-48-64-8)
                    y = random.randint(64+8, settings.screenHeight-48-64-8)
                    self.spawnEnemy(x, y)

    def updateOffset(self, dt):
        self.offset += ((settings.screenWidth//2, settings.screenHeight//2) - self.offset - self.player.rect.center)*dt

    def update(self, dt):
        self.checkEvents()
        self.updateOffset(dt)
        entity.entities.update(dt, self.level.tiles)
    
    def draw(self, surface):
        self.level.draw(surface)
        for e in entity.entities:
            e.draw(surface)