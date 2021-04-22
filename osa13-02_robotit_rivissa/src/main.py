import pygame

pygame.init()
display = pygame.display.set_mode((640, 480))

robo = pygame.image.load('robo.png')

display.fill((0, 0, 0))
for i in range(10):
    display.blit(robo, (50 + 50 * i, 100))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            exit()
