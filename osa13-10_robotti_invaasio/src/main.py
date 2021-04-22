import pygame
from random import randint

pygame.init()
width, height = 640, 480
display = pygame.display.set_mode((width, height))

robo = pygame.image.load('robo.png')

x = 0
y = 0 - robo.get_height()
speed = 2

timer = pygame.time.Clock()

robots = []
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    spawn_robo = randint(1, 100)
    if spawn_robo <= 2:
        robots.append([randint(0, width - robo.get_width()), y])
        if len(robots) > 20:
            robots.pop(0)

    for robodude in robots:
        if robodude[1] + robo.get_height() < height:
            robodude[1] += 1
        elif robodude[0] > width / 2:
            robodude[0] += 1
        else:
            robodude[0] -= 1

    display.fill((0, 0, 0))
    for robodude in robots:
        display.blit(robo, (robodude[0], robodude[1]))
    pygame.display.flip()

    timer.tick(60)
