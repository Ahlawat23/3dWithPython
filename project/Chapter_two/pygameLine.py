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
font = pygame.font.SysFont('Comic Sans MS', 20, False, True)
text = font.render('well we actually print it', True, white)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            if time_clicked == 0:
                point1 = pygame.mouse.get_pos()
            else:
                point2 = pygame.mouse.get_pos()
            time_clicked += 1
            if time_clicked >1:
                pygame.draw.line(screen, white, point1, point2)
                time_clicked = 0
    screen.blit(text, (100, 10))
    pygame.display.update()
pygame.quit()