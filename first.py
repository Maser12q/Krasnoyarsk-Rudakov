import pygame

running = True


# # классы объектов, без них не работает
# class Object:
#     def __init__(self):
#         self.fps = 50
#         self.x_size = width
#         self.y_size = height
#         self.color = (255, 255, 255)
#         self.vi = 50
#         self.r = 70

def k_ku(x, y):
    if y1 < y:
        y -= 1
    elif y1 > y:
        y += 1

    if x1 < x:
        x -= 1
    elif x1 > x:
        x += 1
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 20)

    return x, y


# для настройки окна, типа void Start в Unity или Setup в arduino
pygame.init()
size = width, height = (501, 501)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

x, y = 251, 251
x1, y1 = 251, 251
print(1)
# главный цикл, типа void Update, хотя не, fixed_update, в unity
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x1, y1 = event.pos

    x, y = k_ku(x, y)
    clock.tick(50)
    pygame.display.flip()
