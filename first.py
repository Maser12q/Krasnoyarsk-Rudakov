import pygame


class Object:
    def __init__(self):
        self.fps = 100
        self.x_size = width
        self.y_size = height
        self.vx = -250
        self.vy = -250
        self.color = (255, 255, 255)


class Ball(Object):
    def __init__(self, pos):
        super().__init__()
        self.x, self.y = pos
        pygame.draw.circle(screen, self.color, (self.x, self.y), 10)

    def __delt_v(self):
        if self.x < 10:
            self.x = 10
        if self.x > self.x_size - 10:
            self.x = self.x_size - 10
        if self.y > self.y_size - 10:
            self.y = self.y_size - 10
        if self.y < 10:
            self.y = 10
        if self.x >= self.x_size - 10 or self.x <= 10:
            self.vx = -self.vx
        if self.y >= self.y_size - 10 or self.y <= 10:
            self.vy = -self.vy

        self.x += int(self.vx / self.fps)
        self.y += int(self.vy / self.fps)

    def otr_sob(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 10)
        self.__delt_v()


pygame.init()
size = width, height = (800, 800)
screen = pygame.display.set_mode(size)
n = list()
running = True

clock = pygame.time.Clock()
while running:
    screen.fill((0, 0, 0))
    # pygame.draw.line(screen, (255, 255, 255), (400, 0), (400, 800), 5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            n.append(Ball(event.pos))

    for i in n:
        i.otr_sob()

    clock.tick(100)
    pygame.display.flip()
