import pygame, director, settings

pygame.init()
screen = pygame.display.set_mode( settings.screenSize )
clock = pygame.time.Clock()

jamesGunn = director.Director()
counter = 0

while True:
    dt = clock.tick( settings.frameRate )/1000
    counter += dt
    if counter > 1:
        print(jamesGunn.offset)
        counter = 0
    jamesGunn.update(dt)
    jamesGunn.draw(screen)
    pygame.display.update()