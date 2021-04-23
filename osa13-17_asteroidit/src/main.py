import pygame
from random import randint

pygame.init()
width, height = 640, 480
display = pygame.display.set_mode((width, height))

robo = pygame.image.load("robo.png")
rock = pygame.image.load('kivi.png')

robo_x = int(width / 2 - robo.get_width() / 2)
robo_y = height - robo.get_height()

right = False
left = False

amount = 20
rocks = []
for i in range(amount):
    rocks.append([-1000, height])

ticker = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                right = True
            if event.key == pygame.K_LEFT:
                left = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right = False
            if event.key == pygame.K_LEFT:
                left = False

    if right:
        robo_x += 2
    if left:
        robo_x -= 2

    robo_x = max(robo_x, 0)
    robo_x = min(robo_x, width - robo.get_width())

    for i in range(amount):
        if rocks[i][1] + rock.get_height() < height:
            rocks[i][1] += 1
        else:
            if rocks[i][0] < -rock.get_width() or rocks[i][0] > width:
                rocks[i][0] = randint(0, width - rock.get_width())
                rocks[i][1] = -randint(100, 1000)
    # is it a hit
    for i in range(amount):
        if rocks[i][0] in range(robo_x, robo_x + robo.get_width()) and rocks[i][1] in range(robo_y, robo_y + robo.get_height()):
            print('hit')

        display.fill((0, 0, 0))
        for i in range(amount):
            display.blit(rock, (rocks[i][0], rocks[i][1]))
        display.blit(robo, (robo_x, robo_y))
        pygame.display.flip()

    ticker.tick(60)
