import pygame
from random import randint

# import pygame.locals for easier access to key coordinates
from pygame.locals import (
    RLEACCEL,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

POINTS = 0


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load('../assets/robo.png').convert()
        self.rect = self.image.get_rect(
            center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - self.image.get_height() / 2 - 20)
        )

    # move the player based on user input
    def update(self, keys_pressed) -> None:
        if keys_pressed[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-8, 0)
        if keys_pressed[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(8, 0)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load('../assets/kivi.png').convert()
        self.image.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.image.get_rect(
            center=(
                randint(0, SCREEN_WIDTH),
                -randint(20, 100),
            )
        )

    # move the sprite
    def update(self) -> None:
        self.rect.move_ip(0, 1)


class Floor(pygame.sprite.Sprite):
    def __init__(self):
        super(Floor, self).__init__()
        self.image = pygame.Surface((SCREEN_WIDTH, 20))
        self.image.fill((125, 125, 125))
        self.rect = self.image.get_rect(
            center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 10)
        )


pygame.init()

pygame.font.init()
font = pygame.font.SysFont("FreeSans", 20)

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# background image
bg = pygame.image.load('../assets/bg.jpeg')

# a custom event for adding a new rock. +1 ensures it's going to be unique event
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 2000)

# player instance
robo = Player()
# floor
floor = Floor()

# Groups for enemy sprites(rocks) and all sprites
# - enemies for collision detection and pos updates
# - all_sprites for rendering
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(robo)
all_sprites.add(floor)

running = True
speed = 30

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

        elif event.type == ADDENEMY:
            new_rock = Enemy()
            enemies.add(new_rock)
            all_sprites.add(new_rock)

    # get a set of pressed keys, check for user input and update player pos
    pressed_keys = pygame.key.get_pressed()
    robo.update(pressed_keys)

    # update rock positions
    enemies.update()

    # fill the screen
    screen.fill((0, 0, 0))

    # draw background
    screen.blit(bg, (0, 0))

    # draw all sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    # check if the robot collides with a rock
    for entity in enemies:
        if pygame.sprite.collide_rect(robo, entity):
            entity.kill()
            POINTS += 1
        print(POINTS)

    # check if rock hits the ground
    if pygame.sprite.spritecollideany(floor, enemies):
        running = False

    # update points
    text = font.render(f'pisteet: {POINTS}', True, (255, 255, 255))
    screen.blit(text, (520, SCREEN_HEIGHT - 20))

    # update the screen
    pygame.display.flip()

    # set fps, aka speed
    clock.tick(speed)

# end the game
pygame.quit()
