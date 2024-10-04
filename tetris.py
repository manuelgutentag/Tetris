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

        self.left_collision = False
        self.right_collision = False
        self.bottom_collision = False

    def check_collision(self):
        if self.random == 1:
             for placedblock in self.placed_blocks:
                if int(self.twobytwo[0].x - 1) == placedblock.x and int(self.twobytwo[0].y) == placedblock.y:
                    self.left_collision = True
                elif int(self.twobytwo[1].x - 1) == placedblock.x and int(self.twobytwo[1].y) == placedblock.y:
                    self.left_collision = True

                elif int(self.twobytwo[2].x + 1) == placedblock.x and int(self.twobytwo[2].y) == placedblock.y:
                    self.right_collision = True
                elif int(self.twobytwo[3].x + 1) == placedblock.x and int(self.twobytwo[3].y) == placedblock.y:
                    self.right_collision = True

                elif int(self.twobytwo[0].y + 1) == placedblock.y and int(self.twobytwo[0].x) == placedblock.x:
                    self.bottom_collision = True
                elif int(self.twobytwo[2].y + 1) == placedblock.y and int(self.twobytwo[2].x) == placedblock.x:
                    self.bottom_collision = True

        if self.random == 2: #default rotation
            for placedblock in self.placed_blocks:
                if int(self.ll[0].x - 1) == placedblock.x and int(self.ll[0].y) == placedblock.y:
                    self.left_collision = True
                elif int(self.ll[1].x - 1) == placedblock.x and int(self.ll[1].y) == placedblock.y:
                    self.left_collision = True

                elif int(self.ll[3].x + 1) == placedblock.x and int(self.ll[3].y) == placedblock.y:
                    self.right_collision = True

                elif int(self.ll[1].y + 1) == placedblock.y and int(self.ll[1].x) == placedblock.x:
                    self.bottom_collision = True
                elif int(self.ll[2].y + 1) == placedblock.y and int(self.ll[2].x) == placedblock.x:
                    self.bottom_collision = True
                elif int(self.ll[3].y + 1) == placedblock.y and int(self.ll[3].x) == placedblock.x:
                    self.bottom_collision = True



    def move_block_auto(self):
        if self.random == 1:
            for block in self.twobytwo:
                if block.y < 19.0 and not self.bottom_collision:
                    block.y += 1
                else:
                    self.block_placed = True
                    self.placed_blocks += self.twobytwo
                    print(self.placed_blocks)
                    break

        if self.random == 2:
            for block in self.ll:
                if self.ll[3].y < 19.0:
                    block.y += 1
                else:
                    self.block_placed = True
                    self.placed_blocks += self.ll
                    print(self.placed_blocks)
                    break

    def reset(self):
        self.twobytwo = [Vector2(9, 1), Vector2(9, 0), Vector2(10, 1), Vector2(10, 0)]
        self.ll = [Vector2(8, 0), Vector2(8, 1), Vector2(9, 1), Vector2(10, 1)]
        self.lr = [Vector2(11, 0), Vector2(11, 1), Vector2(10, 1), Vector2(9, 1)]

        self.left_collision = False
        self.right_collision = False
        self.bottom_collision = False

    def collision_reset(self):
        self.left_collision = False
        self.right_collision = False
        self.bottom_collision = False

    def move_block_left(self):
        if self.random == 1:
            if self.twobytwo[0].x > 5 and self.twobytwo[0].y < 19.0 and not self.left_collision:
                self.twobytwo[0].x -= 1
                self.twobytwo[1].x -= 1
                self.twobytwo[2].x -= 1
                self.twobytwo[3].x -= 1
            else:
                print('move_block_left')

        if self.random == 2:
            if self.ll[0].x > 5 and self.ll[1].y < 19.0 and not self.left_collision:
                self.ll[0].x -= 1
                self.ll[1].x -= 1
                self.ll[2].x -= 1
                self.ll[3].x -= 1
            else:
                print('move_block_left')

    def move_block_right(self):
        if self.random == 1:
            if self.twobytwo[2].x < 14 and self.twobytwo[0].y < 19.0 and not self.right_collision:
                self.twobytwo[0].x += 1
                self.twobytwo[1].x += 1
                self.twobytwo[2].x += 1
                self.twobytwo[3].x += 1
            else:
                print('move_block_right')

        if self.random == 2:
            if self.ll[3].x < 14 and self.ll[1].y < 19.0 and not self.right_collision:
                self.ll[0].x += 1
                self.ll[1].x += 1
                self.ll[2].x += 1
                self.ll[3].x += 1
            else:
                print('move_block_right')

    def move_block_down(self):
        if self.random == 1:
            if self.twobytwo[0].y < 19.0 and not self.bottom_collision:
                self.twobytwo[0].y += 1
                self.twobytwo[1].y += 1
                self.twobytwo[2].y += 1
                self.twobytwo[3].y += 1
            else:
                self.block_placed = True
                self.placed_blocks += self.ll
                print(self.placed_blocks)
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

    def fast_feedback(self):
        if self.random == 1:
            for block in self.twobytwo:
                if block.y < 19.0 and not self.bottom_collision:
                    pass
                else:
                    self.block_placed = True
                    self.placed_blocks += self.twobytwo
                    print(self.placed_blocks)
                    break

        if self.random == 2:
            for block in self.ll:
                if self.ll[3].y < 19.0 and not self.bottom_collision:
                    pass
                else:
                    self.block_placed = True
                    self.placed_blocks += self.ll
                    print(self.placed_blocks)
                    break

    def check_row(self):
        # checks for filled rows
        self.x = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        for j in range(20):
            for i in range(len(self.placed_blocks)):
                if self.placed_blocks[i].y == j:
                    self.x[j] += self.placed_blocks[i].x

        for j in range(20):
            for i in range(len(self.placed_blocks)):
                if self.x[j] == 95 and self.placed_blocks[i].y == j:
                    self.placed_blocks[i].x = 0
                    self.placed_blocks[i].y = 0

        for j in range(20):
            for i in range(len(self.placed_blocks)):
                if self.x[j] == 95 and self.placed_blocks[i].y < j and self.placed_blocks[i].y > 0:
                    self.placed_blocks[i].y += 1
        print(self.x)
        for j in range(20):
            self.x[j] = 0



class Main():
    def __init__(self):
        self.block = Blocks()

    def update(self):
        if not self.block.block_placed:
            self.block.move_block_auto()
            self.block.collision_reset()

    def faster_update(self):
        if not self.block.block_placed:
            self.block.fast_feedback()
            self.block.check_collision()
            self.block.check_row()
            #print('left: ' , self.block.left_collision)
            #print('right: ' , self.block.right_collision)
            #print('bottom: ' , self.block.bottom_collision)
        else:
            self.block.reset()
            self.block.random = random.randint(1,2)
            self.block.block_placed = False

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
