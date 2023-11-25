import pygame as pygame
import sys

pygame.init()#kanei initialize to module (einai aparaitito)
screen = pygame.display.set_mode((400,500))#window
clock = pygame.time.Clock()

#main game
while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()#kleinei to game
           sys.exit()
    screen.fill((175,215,70))

    #edw pane ta graphic elements
    pygame.display.update()
    clock.tick(60)#framerate --> 60fps locked :)