import pygame

pygame.init()
display = pygame.display.set_mode((640, 480))

robo = pygame.image.load('robo.png')

x = 0
y = 0
speed = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            exit()

    display.fill((0, 0, 0))
    display.blit(robo, (x, y))
    pygame.display.flip()

    if speed > 0 and x + robo.get_width() < 640:
        x += speed
    elif speed > 0 and y + robo.get_height() < 480:
        y += speed
        if y + robo.get_height() >= 480:
            speed = -speed
    elif speed < 0 and x > 0:
        x += speed
    elif speed < 0 and y > 0:
        y += speed
    else:
        speed = -speed

    clock.tick(60)
