import pygame, director, settings

"""
Easy additions
- Enemy health bars
- Player attacks
- Enemy attacks (player health bar)
- Projectile class
- More animations
- Wave based spawner

Medium additons
- Roguelike mechanics
- Items

"""

pygame.init()
screen = pygame.display.set_mode( settings.screenSize )
clock = pygame.time.Clock()

jamesGunn = director.Director()

while True:
    dt = clock.tick( settings.frameRate )/1000
    #print(jamesGunn.offset)
    jamesGunn.update(dt)
    jamesGunn.draw(screen)
    pygame.display.update()