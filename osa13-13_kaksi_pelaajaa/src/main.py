import pygame

pygame.init()
width, height = 640, 480
display = pygame.display.set_mode((width, height))

sprite = pygame.image.load('robo.png')

# robot positions
robots = [
    [0, height / 2 - sprite.get_height()],
    [width - sprite.get_width(), height / 2 - sprite.get_height()]]

keys = [
    # key pressed, which robot, x-move, y-move
    (pygame.K_LEFT, 0, -2, 0),
    (pygame.K_RIGHT, 0, 2, 0),
    (pygame.K_UP, 0, 0, -2),
    (pygame.K_DOWN, 0, 0, 2),
    (pygame.K_a, 1, -2, 0),
    (pygame.K_d, 1, 2, 0),
    (pygame.K_w, 1, 0, -2),
    (pygame.K_s, 1, 0, 2)
]

timer = pygame.time.Clock()

keys_pressed = {}

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            keys_pressed[event.key] = True

        if event.type == pygame.KEYUP:
            del keys_pressed[event.key]

    for key in keys:
        if key[0] in keys_pressed:
            robots[key[1]][0] += key[2]
            robots[key[1]][1] += key[3]

    display.fill((80, 80, 80))
    for i in range(2):
        display.blit(sprite, (
            min(max(robots[i][0], 0), width - sprite.get_width()),
            min(max(robots[i][1], 0), height - sprite.get_height())))
    pygame.display.flip()

    timer.tick(60)
