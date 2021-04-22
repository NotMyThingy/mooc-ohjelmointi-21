import pygame
from random import randint

pygame.init()

width, height = 640, 480
display = pygame.display.set_mode((width, height))

ball = pygame.image.load("pallo.png")

x = randint(0, width)
y = randint(0, height)
nopeusY = 3
nopeusX = 3

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    display.fill((0, 0, 0))
    display.blit(ball, (x, y))
    pygame.display.flip()

    x += nopeusX
    y += nopeusY

    if x <= 0 or x + ball.get_width() >= width:
        nopeusX = -nopeusX
    if y <= 0 or y + ball.get_height() >= height:
        nopeusY = -nopeusY

    clock.tick(60)
