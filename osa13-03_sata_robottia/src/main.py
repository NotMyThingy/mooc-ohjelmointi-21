import pygame

pygame.init()
display = pygame.display.set_mode((640, 480))

roboman = pygame.image.load('robo.png')

display.fill((0, 0, 0))
for rivi in range(10):
    for sarake in range(10):
        display.blit(roboman, (50 + 40 * sarake + 10 * rivi, 50 + 20 * rivi))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            exit()
