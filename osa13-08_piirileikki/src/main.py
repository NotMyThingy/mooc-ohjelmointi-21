import pygame
import math

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

kulma = 0
kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((0, 0, 0))
    for i in range(10):
        naytto.blit(robo, (320 + math.cos(kulma + 0.628 * i) * 150 - robo.get_width() / 2,
                           240 + math.sin(kulma + 0.628 * i) * 150 - robo.get_height() / 2))
    pygame.display.flip()

    kulma += 0.01
    kello.tick(60)
