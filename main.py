import pygame, director, settings

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode( settings.screenSize )
clock = pygame.time.Clock()

jamesGunn = director.Director()

while True:
    dt = clock.tick( settings.frameRate )/1000
    #print(jamesGunn.offset)
    jamesGunn.update(dt)
    jamesGunn.draw(screen)
    pygame.display.update()