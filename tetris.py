import pygame,sys,random
from pygame.math import Vector2

class Blocks():
    def __init__(self):
        self.twobytwo = [Vector2(10,1), Vector2(10,0), Vector2(11,1), Vector2(11,0)]

    def move_block(self):
        for block in self.twobytwo:
            if block.y > 18.0:
                break
            block.y += 1
            twobytwo_rect = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size, cell_size)
            pygame.draw.rect(screen, (0,250,0), twobytwo_rect)
            print(block.y)

    def draw_newblock(self):
        for block in self.twobytwo:
            twobytwo_rect = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size, cell_size)
            pygame.draw.rect(screen, (250,0,0), twobytwo_rect)

class Main():
    def __init__(self):
        self.block = Blocks()

    def update(self):
        self.block.move_block()

    def draw_game_elements(self):
        self.block.draw_newblock()
        self.draw_sidelines()

    def draw_sidelines(self):
        sideline_rect_l = pygame.Rect(0,0, cell_size * 5, cell_size * 20)
        sideline_rect_r = pygame.Rect(cell_size * 15, 0, cell_size * 5, cell_size * 20)
        pygame.draw.rect(screen, (125,125,125), sideline_rect_l)
        pygame.draw.rect(screen, (125,125,125), sideline_rect_r)


pygame.init()
cell_size = 90
cell_count_vert = 20
cell_count_hor = 20
screen = pygame.display.set_mode((cell_size*cell_count_hor, cell_size*cell_count_vert))
clock = pygame.time.Clock()

screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update, 500)

main = Main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            sys.exit()
        if event.type == screen_update:
            main.update()

    screen.fill((0,0,0))
    main.draw_game_elements()

    pygame.display.update()
    clock.tick(60)
