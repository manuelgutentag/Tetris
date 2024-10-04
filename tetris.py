import pygame,sys,random
from pygame.math import Vector2

class Blocks():
    def __init__(self):
        #self.random = random.randint(1,3)
        self.random = random.randint(1,2)
        self.twobytwo = [Vector2(9, 1), Vector2(9, 0), Vector2(10, 1), Vector2(10, 0)]
        self.ll = [Vector2(8, 0), Vector2(8, 1), Vector2(9, 1), Vector2(10, 1)]
        self.lr = [Vector2(11, 0), Vector2(11, 1), Vector2(10, 1), Vector2(9, 1)]

        self.placed_blocks = []
        self.block_placed = False

    def move_block_auto(self):
        if self.random == 1:
            for block in self.twobytwo:
                if block.y < 19.0:
                    block.y += 1
                    twobytwo_rect = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size, cell_size)
                    pygame.draw.rect(screen, (0, 250, 0), twobytwo_rect)
                else:
                    self.block_placed = True
                    self.placed_blocks += self.twobytwo
                    print(self.placed_blocks)
                    break

        if self.random == 2:
            for block in self.ll:
                if self.ll[3].y < 19.0:
                    block.y += 1
                    ll_rect = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size, cell_size)
                    pygame.draw.rect(screen, (0, 250, 0), ll_rect)
                else:
                    self.block_placed = True
                    self.placed_blocks += self.ll
                    print(self.placed_blocks)
                    break

    def reset(self):
        self.twobytwo = [Vector2(9, 1), Vector2(9, 0), Vector2(10, 1), Vector2(10, 0)]
        self.ll = [Vector2(8, 0), Vector2(8, 1), Vector2(9, 1), Vector2(10, 1)]
        self.lr = [Vector2(11, 0), Vector2(11, 1), Vector2(10, 1), Vector2(9, 1)]

    def move_block_left(self):
        if self.random == 1:
            if self.twobytwo[0].x > 5 and self.twobytwo[0].y < 19.0:
                self.twobytwo[0].x -= 1
                self.twobytwo[1].x -= 1
                self.twobytwo[2].x -= 1
                self.twobytwo[3].x -= 1
            else:
                print('move_block_left')

        if self.random == 2:
            if self.ll[0].x > 5 and self.ll[1].y < 19.0:
                self.ll[0].x -= 1
                self.ll[1].x -= 1
                self.ll[2].x -= 1
                self.ll[3].x -= 1
            else:
                print('move_block_left')

    def move_block_right(self):
        if self.random == 1:
            if self.twobytwo[2].x < 14 and self.twobytwo[0].y < 19.0:
                self.twobytwo[0].x += 1
                self.twobytwo[1].x += 1
                self.twobytwo[2].x += 1
                self.twobytwo[3].x += 1
            else:
                print('move_block_right')

        if self.random == 2:
            if self.ll[3].x < 14 and self.ll[1].y < 19.0:
                self.ll[0].x += 1
                self.ll[1].x += 1
                self.ll[2].x += 1
                self.ll[3].x += 1
            else:
                print('move_block_right')

    def move_block_down(self):
        if self.random == 1:
            if self.twobytwo[0].y < 19.0:
                self.twobytwo[0].y += 1
                self.twobytwo[1].y += 1
                self.twobytwo[2].y += 1
                self.twobytwo[3].y += 1
            else:
                print('move_block_down')

        if self.random == 2:
            if self.ll[1].y < 19.0:
                self.ll[0].y += 1
                self.ll[1].y += 1
                self.ll[2].y += 1
                self.ll[3].y += 1
            else:
                print('move_block_down')

    def draw_block(self):
        if self.random == 1:
            for block in self.twobytwo:
                twobytwo_rect = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size, cell_size)
                pygame.draw.rect(screen, (250,0,0), twobytwo_rect)
        if self.random == 2:
            for block in self.ll:
                ll_rect = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size, cell_size)
                pygame.draw.rect(screen, (250,0,0), ll_rect)

    def draw_placed_blocks(self):
        for block in self.placed_blocks:
            placed_blocks_rect = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size, cell_size)
            pygame.draw.rect(screen, (0,240,100), placed_blocks_rect)

    def fast(self):
        pass

class Main():
    def __init__(self):
        self.block = Blocks()

    def update(self):
        if not self.block.block_placed:
            self.block.move_block_auto()
        else:
            self.block.reset()
            self.block.random = random.randint(1,2)
            self.block.block_placed = False

    def faster_update(self):
        self.block.fast()

    def draw_game_elements(self):
        self.block.draw_block()
        self.block.draw_placed_blocks()
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
clock2 = pygame.time.Clock()
pygame.key.set_repeat(200, 40) # für Taste gedrückt halten


screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update, 900)

main = Main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            sys.exit()
        if event.type == screen_update:
            main.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and not main.block.block_placed:
                main.block.move_block_left()
            if event.key == pygame.K_d and not main.block.block_placed:
                main.block.move_block_right()
            if event.key == pygame.K_s and not main.block.block_placed:
                main.block.move_block_down()

    screen.fill((0,0,0))
    main.draw_game_elements()
    main.faster_update()

    pygame.display.update()
    clock.tick(60)
