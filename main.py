import pygame, sys

pygame.init()

#screen setup
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
black = 0, 0, 0

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    screen.fill(black)




