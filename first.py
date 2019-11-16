import pygame

pygame.init()
size = width, height = tuple(map(int, input().split()))
screen = pygame.display.set_mode(size)

pygame.draw.rect(screen, (255, 0, 0), (1, 1, width - 2, height - 2))
pygame.display.flip()

# ожидание закрытия окна:
while pygame.event.wait().type != pygame.QUIT:
    pass
