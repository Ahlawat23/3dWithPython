import pygame

pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

done = False
white = pygame.Color(255, 255, 255)

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.rect(screen, white, (900, 250, 15, 15))
    pygame.draw.rect(screen, white, (820, 200, 7, 7))
    pygame.draw.rect(screen, white, (590, 270, 5, 5))
    pygame.draw.rect(screen, white, (570, 600, 20, 20))
    pygame.draw.rect(screen, white, (550, 330, 25, 25))
    pygame.draw.rect(screen, white, (300, 580, 5, 5))
    pygame.draw.rect(screen, white, (280, 350, 27, 27))
    pygame.draw.rect(screen, white, (150, 560, 21, 21))
    pygame.display.update()

pygame.quit()
