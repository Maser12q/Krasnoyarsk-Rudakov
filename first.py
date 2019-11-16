import pygame

pygame.init()
width, n = tuple(map(int, input().split()))
height = width
size = width, height
screen = pygame.display.set_mode(size)

for i in range(n):
    for j in range(n):
        if (j + i) % (2 * n) != 0:
            pygame.draw.rect(screen, (0, 0, 0), (i, j, n, n))
            # print(i, j)
        else:
            pygame.draw.rect(screen, (255, 255, 255), (i, j, n, n))

            # print('*' * 40)

pygame.display.flip()

# ожидание закрытия окна:
while pygame.event.wait().type != pygame.QUIT:
    pass
