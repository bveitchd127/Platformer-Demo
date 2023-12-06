import pygame, director, settings

pygame.init()
screen = pygame.display.set_mode( settings.screenSize )
clock = pygame.time.Clock()

jamesGunn = director.Director()

while True:
    dt = clock.tick( settings.frameRate )/1000
    jamesGunn.update(dt)
    jamesGunn.draw(screen)
    pygame.display.update()