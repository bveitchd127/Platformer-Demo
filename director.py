import pygame, sys, settings, level, player, entity, enemy, random

class Director:
    def __init__(self):
        """
        Director is responsible for all game mechanics
        """
        self.level = level.Level("level1.txt")
        self.player = player.Player(self, 100,100)
        self.enemies = pygame.sprite.Group()
    
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
                    x = random.randint(64+8, settings.screenWidth-48-64-8)
                    y = random.randint(64+8, settings.screenHeight-48-64-8)
                    self.enemies.add( enemy.Enemy(self,x,y) )


    
    def update(self, dt):
        self.checkEvents()
        entity.entities.update(dt, self.level.tiles)
    
    def draw(self, surface):
        self.level.draw(surface)
        for e in entity.entities:
            e.draw(surface)