import pygame

pygame.init()
display = pygame.display.set_mode((640, 480))

mr_robot = pygame.image.load('robo.png')

display.fill((0, 0, 0))
display.blit(mr_robot, (0, 0))
display.blit(mr_robot, (640 - mr_robot.get_width(), 0))
display.blit(mr_robot, (0, 480 - mr_robot.get_height()))
display.blit(mr_robot, (640 - mr_robot.get_width(), 480 - mr_robot.get_height()))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
