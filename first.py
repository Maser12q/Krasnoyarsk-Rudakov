import pygame

width, n = tuple(map(int, input().split()))

pron = n % 2 != 1
kol_vo = width // n
size = width, width

pygame.init()
screen = pygame.display.set_mode(size)

for i in range(0, width + kol_vo, kol_vo):
    for j in range(0, width, kol_vo):
        if (j + i) % (2 * kol_vo) != 0:
            pygame.draw.rect(screen, (255, 255, 255), (i - (kol_vo * pron), j, kol_vo, kol_vo))
pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass
