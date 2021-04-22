import pygame
import time
import math

pygame.init()
display = pygame.display.set_mode((640, 480))
display_time = ''

angle_sec = 270 * 0.0174533
angle_min = 240 * 0.0174533
angle_hour = 140.1 * 0.0174533
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    sec_x = 319 + math.cos(angle_sec) * 190
    sec_y = 240 + math.sin(angle_sec) * 190
    min_x = 318 + math.cos(angle_min) * 185
    min_y = 240 + math.sin(angle_min) * 185
    hour_x = 316 + math.cos(angle_hour) * 175
    hour_y = 240 + math.sin(angle_hour) * 175

    pygame.draw.rect(display, (0, 0, 0), (0, 0, 640, 480))
    pygame.draw.circle(display, (255, 0, 0), (320, 240), 200, 5)
    pygame.draw.line(display, (0, 0, 255), (319, 240), (sec_x, sec_y), 1)
    pygame.draw.line(display, (0, 0, 255), (318, 240), (min_x, min_y), 2)
    pygame.draw.line(display, (0, 0, 255), (316, 240), (hour_x, hour_y), 4)
    pygame.draw.circle(display, (255, 0, 0), (320, 240), 10)
    pygame.display.flip()

    angle_sec += 0.104719755
    angle_min += 0.001745329
    angle_hour += 
    clock.tick(1)
