import pygame

pygame.init()
width, n = 900, 4  # tuple(map(int, input().split()))
height = width
size = width, height
screen = pygame.display.set_mode(size)

kol_vo = width // n
for i in range(n):
    for j in range(n):
        if (j + i) % 2 != 0:
            pygame.draw.rect(screen, (255, 255, 255), (i * kol_vo, j * kol_vo, kol_vo, kol_vo))
            print(i, j)
        # else:
        #     pygame.draw.rect(screen, (0, 0, 0), (i + kol_vo, j + kol_vo, kol_vo, kol_vo))
        #
        #     print(i, j)

pygame.display.flip()

# ожидание закрытия окна:
while pygame.event.wait().type != pygame.QUIT:
    pass
