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

    y += speed
    if speed > 0 and y + robo.get_height() >= 480:
        speed = -speed
    elif y <= 0:
        speed = -speed
    clock.tick(60)
