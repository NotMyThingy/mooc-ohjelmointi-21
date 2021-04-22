import pygame

pygame.init()
width, height = 640, 480
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('osa13-14_robotti_ja_hiiri')

das_robo = pygame.image.load('robo.png')

robo_x, robo_y = 0, 0
mouse_x, mouse_y = 0, 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.MOUSEMOTION:
            mouse_x = event.pos[0] - das_robo.get_width() / 2
            mouse_y = event.pos[1] - das_robo.get_height() / 2

            robo_x = min(max(mouse_x, 0), width - das_robo.get_width())
            robo_y = min(max(mouse_y, 0), height - das_robo.get_height())

            display.fill((0, 0, 0))
            display.blit(das_robo, (robo_x, robo_y))
            pygame.display.flip()
