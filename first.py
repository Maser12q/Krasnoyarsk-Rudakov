"""С клавиатуры вводится толщина кольца N (в пикселях) и количество колец K.
Нарисуйте «RGB мишень» из внутреннего круга и K колец чистого
красного, зеленого, синего, красного и т.д. («по кругу») цветов максимальной яркости.
Радиус маленького красного круга и толщина каждого кольца должны быть равны N пикселей.
Мишень должна быть прижата к левому верхнему краю окна."""

import pygame

"""место для объявления переменных"""
q = 1

n, k = map(int, input().split())
size = 2 * n * k, 2 * n * k

# Начало отрисовки окна
pygame.init()
screen = pygame.display.set_mode(size)
for i in range(k, 0, -1):
    us1, us2, us3 = (k - q) % 3 == 1, (k - q) % 3 == 2, (k - q) % 3 == 0
    pygame.draw.circle(screen, (255 * us3, 255 * us1, 255 * us2), (n * k, n * k), (n * i))
    pygame.draw.circle(screen, (255 * us3, 255 * us1, 255 * us2), (0, n * k), (n * i))
    pygame.draw.circle(screen, (255 * us3, 255 * us1, 255 * us2), (n * k, 0), (n * i))
    pygame.draw.circle(screen, (255 * us3, 255 * us1, 255 * us2), (n * k * 2, n * k), (n * i))
    pygame.draw.circle(screen, (255 * us3, 255 * us1, 255 * us2), (n * k, n * k * 2), (n * i))
    if q + 1 > 3:
        q = 1
    else:
        q += 1

pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass
