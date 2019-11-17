import pygame

"""место для объявления переменных"""
# n = 100  # int(input())
size = 300, 200


# Начало отрисовки окна
pygame.init()
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))

for i in range(300 // 15):
    for j in range(200 // 15):
        if j % 2 == 0:
            pygame.draw.rect(screen, (255, 0, 0), (i * 33, j + (17 * j), 31, 16))
        else:
            pygame.draw.rect(screen, (255, 0, 0), (-15 + (i * 33), j + (17 * j), 31, 16))

pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass
