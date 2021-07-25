from math import sqrt
import pygame
pygame.init()
class Board:
    def __init__(self, screen, quan):
        self.quan = int(sqrt(quan))
        self.width = screen
        self.height = screen
        self.board = [[0] * int(sqrt(quan)) for _ in range(int(sqrt(quan)))]
        self.cell_size = screen / int(sqrt(quan))
    def render(self, screen):
        cnt = 0
        for i in range(self.quan):
            for j in range(self.quan):
                if cnt % 2:
                    pygame.draw.rect(screen, 'white', (self.cell_size * i,self.cell_size * j, self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(screen, 'black', (self.cell_size * i, self.cell_size * j, self.cell_size, self.cell_size))
                cnt+=1
            cnt-=1
a = int(input())
b = int(input())
board = Board(a, b)
size = w, h = a, a
screen = pygame.display.set_mode(size)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
