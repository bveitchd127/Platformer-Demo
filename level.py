import pygame, settings, tile

class Level:
    def __init__(self, director, fileName):
        self.director = director
        self.tiles = pygame.sprite.Group()
        self.loadLevel(fileName)

    def loadLevel(self, fileName):
        numOfTiles = 0
        # Open a text file
        with open("levels/" + fileName) as fin:
            # Loop through each row in the text file
            for y,line in enumerate( fin.readlines() ):
                # Loops through each character in a row
                for x,col in enumerate( line ):
                    cx, cy = x*settings.tileSize, y*settings.tileSize
                    # If the character is an X, then place a tile at that position
                    if col == "X":
                        self.tiles.add( tile.Tile(cx, cy, settings.tileColor) )
                        numOfTiles+=1
                    elif col == "P":
                        self.tiles.add( tile.Tile(cx, cy, settings.pipeColor) )
                        numOfTiles+=1
                    elif col == "?":
                        self.tiles.add( tile.Tile(cx, cy, settings.powerupColor) )
                        numOfTiles+=1
        print(numOfTiles)
                    
    def draw(self, surface):
        surface.fill(settings.backgroundColor)
        for t in self.tiles:
            surface.blit(t.image, t.rect.topleft + self.director.offset)
