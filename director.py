import pygame, sys, settings, level, player, entity, enemy, random

class Director:
    def __init__(self):
        """
        Director is responsible for all game mechanics
        """
        self.level = level.Level(self, "level2.txt")
        self.player = player.Player(self, 100,100)
        self.enemies = pygame.sprite.Group()
        self.offset = pygame.math.Vector2(self.player.rect.center)
    
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
                    self.enemies.add( enemy.Enemy(self,x,y) )

    def updateOffset(self, dt):
        self.offset += settings.cameraFollowSpeed*((640,360) - self.offset - self.player.rect.center)*dt
        self.offset.y = pygame.math.clamp(self.offset.y, -48, 2000)
        self.offset.x = pygame.math.clamp(self.offset.x, -8928, -48)

    def checkPlayerFall(self):
        if self.player.rect.y > 5000:
            print("Respawning player")
            self.player.rect.center = (100,100)

    def update(self, dt):
        self.checkEvents()
        self.checkPlayerFall()
        self.updateOffset(dt)
        entity.entities.update(dt, self.level.tiles)
    
    def draw(self, surface):
        self.level.draw(surface)
        for e in entity.entities:
            e.draw(surface)