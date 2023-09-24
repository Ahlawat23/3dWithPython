import pygame
from pygame.locals import *

pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

done = False
white = pygame.Color(255, 255, 255)
time_clicked = 0

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            if time_clicked == 0:
                point1 = pygame.mouse.get_pos()
            elif time_clicked == 1:
                point2 = pygame.mouse.get_pos()
            else:
                point3 = pygame.mouse.get_pos()
            time_clicked += 1
            if time_clicked > 2:
                pygame.draw.polygon(screen, white, (point1, point2, point3))
                time_clicked = 0


    pygame.display.update()
pygame.quit()