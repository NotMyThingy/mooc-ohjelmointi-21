import pygame
import math
from datetime import datetime

pygame.init()
display = pygame.display.set_mode((640, 480))


def circle(color: tuple, radius: int, thickness: int = 0):
    pygame.draw.circle(display, color, (320, 240), radius, thickness)


def pointer(length: int, thickness: int, division: float):
    angle = 2 * math.pi * division - math.pi / 2
    x = 320 + math.cos(angle) * length
    y = 240 + math.sin(angle) * length

    pygame.draw.line(display, (0, 0, 225), (320, 240), (x, y), thickness)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    hh = datetime.now().hour % 12
    mm = datetime.now().minute
    ss = datetime.now().second

    display.fill((0, 0, 0))

    circle((255, 0, 0), 200, 5)
    pointer(190, 1, ss / 60)
    pointer(180, 2, (mm + ss / 60) / 60)
    pointer(150, 6, (hh + mm / 60 + ss / 3600) / 12)
    circle((255, 0, 0), 10, )

    pygame.display.set_caption(str(datetime.now().time())[:8])
    pygame.display.flip()
