import pygame

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

pygame.draw.line(screen, (255, 255, 255), (0, 600), (800, 0), 5)
pygame.draw.line(screen, (255, 255, 255), (0, 0), (800, 600), 5)
pygame.display.flip()
# ожидание закрытия окна:
while pygame.event.wait().type != pygame.QUIT:
    pass
