import pygame
from pygame.math import Vector2

"""классы объектов, без них не работает"""


class Object:
    def __init__(self):
        self.fps = 50
        self.x_size = width
        self.y_size = height
        self.color = (255, 255, 255)
        self.vi = 50
        self.r = 70


class Threeangle(Object):
    def __init__(self, a1, a2):
        super().__init__()
        self.angle_1 = a1
        self.angle_2 = a2
        self.vt = 0
        self.a1 = Vector2((101, self.r))

        self.a2 = Vector2((101, self.r))

        print(self.vt)

    def low_v(self):
        self.vt -= self.vi

    def high_v(self):
        self.vt += self.vi

    def edit_angle(self):
        self.angle_1 += int(self.vt / self.fps) * 3
        self.angle_2 += int(self.vt / self.fps) * 3
        self.a1.from_polar((self.r, self.angle_1))
        self.a2.from_polar((self.r, self.angle_2))

    def change_koord(self):
        self.edit_angle()
        pygame.draw.polygon(screen, (255, 255, 255), [(101, 101), self.a1 + (101, 101), self.a2 + (101, 101)])
        # print(self.vt)


"""для настройки окна, типа void Start в Unity"""
pygame.init()
size = width, height = (201, 201)
screen = pygame.display.set_mode(size)
running = True
clock = pygame.time.Clock()
n = [Threeangle(255, 285), Threeangle(15, 45), Threeangle(165, 135)]

"""главный цикл, типа void Update, хотя не, fixed_update, в unity"""
while running:
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), (101, 101), 10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # down
                for i in n:
                    i.low_v()
            elif event.button == 3:
                # up
                for i in n:
                    i.high_v()

    for i in n:
        i.change_koord()
        # print(i.vt)

    clock.tick(50)
    pygame.display.flip()
