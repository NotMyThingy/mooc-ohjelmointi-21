import pygame

pygame.init()
width, height = 640, 480
display = pygame.display.set_mode((width, height))

robo = pygame.image.load('robo.png')

x = width / 2 - robo.get_width() / 2
y = height / 2 - robo.get_height() / 2

left = False
right = False
up = False
down = False

timer = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_RIGHT:
                right = True
            if event.key == pygame.K_UP:
                up = True
            if event.key == pygame.K_DOWN:
                down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_RIGHT:
                right = False
            if event.key == pygame.K_UP:
                up = False
            if event.key == pygame.K_DOWN:
                down = False

    if left and x > 0:
        x -= 2
    if right and x < width - robo.get_width():
        x += 2
    if up and y > 0:
        y -= 2
    if down and y < height - robo.get_height():
        y += 2

    display.fill((80, 80, 80))
    display.blit(robo, (x, y))
    pygame.display.flip()

    timer.tick(60)
