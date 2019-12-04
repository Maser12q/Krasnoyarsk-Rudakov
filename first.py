import os
import random

import pygame


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


size = width, height = 400, 300
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

bomb_image = load_image("bomb.png")

for i in range(50):
    bomb = pygame.sprite.Sprite(all_sprites)
    bomb.image = bomb_image
    bomb.rect = bomb.image.get_rect()

    bomb.rect.x = random.randrange(width)
    bomb.rect.y = random.randrange(height)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.Color("white"))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
