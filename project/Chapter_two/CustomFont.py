import pygame
from pygame.locals import *

pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

done = False
white = pygame.Color(255, 255, 255)
time_clicked = 0

pygame.font.init()
font = pygame.font.Font('Blazed.ttf', 40)
fontTwo = pygame.font.SysFont('comicsansms', 40)
text = font.render('well we actually print it', True, white)
textTwo = fontTwo.render("the second text", False, pygame.Color(10, 255, 0))

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(text, (100, 10))
    screen.blit(textTwo, (10, 50))
    pygame.display.update()
pygame.quit()