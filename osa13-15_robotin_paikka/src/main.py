import pygame
from random import randint

pygame.init()
width, height = 640, 480
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('osa13-15_robotin_paikka')

robo = pygame.image.load('robo.png')

robo_x = randint(0, width - robo.get_width())
robo_y = randint(0, height - robo.get_height())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            if mouse_x in range(robo_x, robo_x + robo.get_width()) \
                    and mouse_y in range(robo_y, robo_y + robo.get_height()):
                robo_x = randint(0, width - robo.get_width())
                robo_y = randint(0, height - robo.get_height())

        display.fill((0, 0, 0))
        display.blit(robo, (robo_x, robo_y))
        pygame.display.flip()
