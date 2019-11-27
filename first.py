import random

import pygame

# width, height =
size = 1000, 1000
fps = 60
screen = pygame.display.set_mode(size)
running = True
clock = pygame.time.Clock()


def get_col():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = dict()  # (cell_x, cell_y): [cell_id, cell_val]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, surf):
        for i in range(self.left, self.left + self.width * self.cell_size, self.cell_size):
            for j in range(self.top, self.top + self.height * self.cell_size, self.cell_size):
                if (i, j) not in self.board.keys():
                    self.board[(i, j)] = [(i // self.cell_size, j // self.cell_size), 0]
                if self.board[(i, j)][1] != 1:
                    pygame.draw.rect(surf, (255, 255, 255), (i, j, self.cell_size, self.cell_size), 1)
                else:
                    pygame.draw.rect(surf, (255, 255, 255), (i, j, self.cell_size, self.cell_size))

    def get_cell(self, mouse_pos):
        xm, ym = mouse_pos
        for xc, yc in self.board.keys():
            if xc <= xm <= xc + self.cell_size and yc <= ym <= yc + self.cell_size:
                return xc, yc

    def on_click(self, cell_coords):
        if cell_coords is not None:
            x, y = cell_coords
            if self.board[(x, y)][1] == 1:
                self.board[(x, y)][1] = 0
            else:
                self.board[(x, y)][1] = 1

    def get_click(self, mouse_pos):
        self.on_click(self.get_cell(mouse_pos))


board = Board(10, 10)

board.set_view(0, 0, 50)

while running:
    screen.fill((0, 0, 0))
    board.render(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
        if event.type == pygame.KEYDOWN:
            board.board.clear()
    screen.fill((0, 0, 0))
    board.render(screen)
    clock.tick(fps)
    pygame.display.flip()

print(board.board)
