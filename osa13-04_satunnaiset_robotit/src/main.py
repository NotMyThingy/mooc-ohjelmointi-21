import pygame
from random import randint

pygame.init()
display = pygame.display.set_mode((640, 480))

roboman = pygame.image.load('robo.png')

display.fill((0, 0, 0))
for i in range(1000):
    display.blit(roboman, (randint(0, 640 - roboman.get_width()), randint(0, 480 - roboman.get_height())))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            exit()
