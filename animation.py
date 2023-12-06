import pygame

class Animation:
    def __init__(self, sourceFile, frameRate, offset = (0,0)):
        self.frameRate = frameRate
        self.frames = []
        self.frameTimer = 0.0

        sourceFrame = pygame.image.load(sourceFile).convert_alpha()
        self.frameCount = sourceFrame.get_width() // sourceFrame.get_height()
        frameSize = (sourceFrame.get_height(), sourceFrame.get_height())

        for i in range(self.frameCount):
            # 48*i for x value for each frame
            newFrame = pygame.Surface(frameSize, pygame.SRCALPHA)
            newFrame.blit(sourceFrame, offset, pygame.Rect((sourceFrame.get_height()*i,0), frameSize))
            self.frames.append(newFrame)

    def update(self, dt):
        self.frameTimer += self.frameRate*dt
    
    def getFrame(self):
        return self.frames[ int(self.frameTimer)%self.frameCount ]
