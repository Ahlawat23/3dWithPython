import pygame
from pygame.locals import *

pygame.init()
screen_width = 1200
screen_height = 575
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('A beautifull senset')
background = pygame.image.load('sunset.jpeg')

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(background, (0, 0))
    pygame.display.update()
pygame.quit()