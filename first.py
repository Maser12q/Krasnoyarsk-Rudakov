import pygame

pygame.init()
width, n = tuple(map(int, input().split()))
height = width
kol_vo = width // n
size = width, height

screen = pygame.display.set_mode(size)

for i in range(0, width + kol_vo, kol_vo):
    for j in range(0, width + kol_vo, kol_vo):
        if n % 2 != 1:
            if (j + i) % (2 * kol_vo) != 0:
                pygame.draw.rect(screen, (255, 255, 255), (i - kol_vo, j, kol_vo, kol_vo))
        else:
            if (j + i) % (2 * kol_vo) != 0:
                pygame.draw.rect(screen, (255, 255, 255), (i, j, kol_vo, kol_vo))

pygame.display.flip()

# ожидание закрытия окна:
while pygame.event.wait().type != pygame.QUIT:
    pass
