import pygame

pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

done = False
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)

xoriginoffset = int(screen.get_width() / 2)
yoriginoffset = int(screen.get_height() / 2)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.update()
pygame.quit()