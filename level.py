import pygame, settings, tile

class Level:
    def __init__(self, director, fileName):
        self.director = director
        self.tiles = pygame.sprite.Group()
        self.spawnPoint = (0,0)
        self.loadLevel(fileName)
        

    def loadLevel(self, fileName):
        # Open a text file
        with open("levels/" + fileName) as fin:
            # Loop through each row in the text file
            for y,line in enumerate( fin.readlines() ):
                # Loops through each character in a row
                for x,col in enumerate( line ):
                    # If the character is an X, then place a tile at that position
                    if col == "X":
                        self.tiles.add( tile.Tile(x*settings.tileSize, y*settings.tileSize) )
                    if col == "P":
                        self.director.player.rect.topleft = (x*settings.tileSize, y*settings.tileSize)
                    if col == "E":
                        self.director.spawnEnemy(x*settings.tileSize, y*settings.tileSize)
                    if col == "S":
                        self.spawnPoint = (x*settings.tileSize, y*settings.tileSize)
                        
                    
    def draw(self, surface):
        surface.fill(settings.backgroundColor)
        #self.tiles.draw(surface)
        for t in self.tiles:
            surface.blit(t.image, t.rect.topleft + self.director.offset)
