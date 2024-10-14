import pygame,sys,random
from pygame.math import Vector2

class Blocks():
    def __init__(self):
        self.blocksfrozen = True
        self.score = 0
        self.level = 0
        self.current_block = random.randint(1,2)
        self.next_block = random.randint(1,2)
        self.current_rotation = 1
        self.twobytwo = [Vector2(9, 1), Vector2(9, 0), Vector2(10, 1), Vector2(10, 0)]
        self.ll = [Vector2(8, 0), Vector2(8, 1), Vector2(9, 1), Vector2(10, 1)]
        self.lr = [Vector2(11, 0), Vector2(11, 1), Vector2(10, 1), Vector2(9, 1)]

        self.twobytwo_next = [Vector2(9, 1), Vector2(9, 0), Vector2(10, 1), Vector2(10, 0)]
        self.ll_next = [Vector2(8, 0), Vector2(8, 1), Vector2(9, 1), Vector2(10, 1)]

        self.placed_blocks = []
        self.block_placed = False

        self.left_collision = False
        self.right_collision = False
        self.bottom_collision = False

        self.tick = False
        self.blockscleared = 0
        self.totalblockscleared = 0
        self.firstclear = False
        self.settimerflag = False

    def rotate(self):
        if self.current_block == 2:
            if self.current_rotation == 1:
                self.ll[0] += Vector2(2,0)
                self.ll[1] += Vector2(1,-1)
                self.ll[2] += Vector2(0,0)
                self.ll[3] += Vector2(-1,1)

            if self.current_rotation == 2:
                self.ll[0] += Vector2(0,2)
                self.ll[1] += Vector2(1,1)
                self.ll[2] += Vector2(0,0)
                self.ll[3] += Vector2(-1,-1)

            if self.current_rotation == 3:
                self.ll[0] += Vector2(-2,0)
                self.ll[1] += Vector2(-1,1)
                self.ll[2] += Vector2(0,0)
                self.ll[3] += Vector2(1,-1)

            if self.current_rotation == 4:
                self.ll[0] += Vector2(0,-2)
                self.ll[1] += Vector2(-1,-1)
                self.ll[2] += Vector2(0,0)
                self.ll[3] += Vector2(1,1)

    def check_collision(self):
        self.bottom_collision = False
        if self.current_block == 1:
             for placedblock in self.placed_blocks:
                if int(self.twobytwo[0].x - 1) == placedblock.x and int(self.twobytwo[0].y) == placedblock.y:
                    self.left_collision = True
                elif int(self.twobytwo[1].x - 1) == placedblock.x and int(self.twobytwo[1].y) == placedblock.y:
                    self.left_collision = True

                if int(self.twobytwo[2].x + 1) == placedblock.x and int(self.twobytwo[2].y) == placedblock.y:
                    self.right_collision = True
                elif int(self.twobytwo[3].x + 1) == placedblock.x and int(self.twobytwo[3].y) == placedblock.y:
                    self.right_collision = True

                if int(self.twobytwo[0].y + 1) == placedblock.y and int(self.twobytwo[0].x) == placedblock.x:
                    self.bottom_collision = True
                elif int(self.twobytwo[2].y + 1) == placedblock.y and int(self.twobytwo[2].x) == placedblock.x:
                    self.bottom_collision = True

        if self.current_block == 2: #default rotation
            if self.current_rotation == 1:
                for placedblock in self.placed_blocks:
                    if int(self.ll[0].x - 1) == placedblock.x and int(self.ll[0].y) == placedblock.y:
                        self.left_collision = True
                    elif int(self.ll[1].x - 1) == placedblock.x and int(self.ll[1].y) == placedblock.y:
                        self.left_collision = True

                    if int(self.ll[3].x + 1) == placedblock.x and int(self.ll[3].y) == placedblock.y:
                        self.right_collision = True

                    if int(self.ll[1].y + 1) == placedblock.y and int(self.ll[1].x) == placedblock.x:
                        self.bottom_collision = True
                    elif int(self.ll[2].y + 1) == placedblock.y and int(self.ll[2].x) == placedblock.x:
                        self.bottom_collision = True
                    elif int(self.ll[3].y + 1) == placedblock.y and int(self.ll[3].x) == placedblock.x:
                        self.bottom_collision = True

            if self.current_rotation == 2:
                for placedblock in self.placed_blocks:
                    if int(self.ll[1].x - 1) == placedblock.x and int(self.ll[1].y) == placedblock.y:
                        self.left_collision = True
                    elif int(self.ll[2].x - 1) == placedblock.x and int(self.ll[2].y) == placedblock.y:
                        self.left_collision = True
                    elif int(self.ll[3].x - 1) == placedblock.x and int(self.ll[3].y) == placedblock.y:
                        self.left_collision = True

                    if int(self.ll[0].x + 1) == placedblock.x and int(self.ll[0].y) == placedblock.y:
                        self.right_collision = True
                    elif int(self.ll[2].x + 1) == placedblock.x and int(self.ll[2].y) == placedblock.y:
                        self.right_collision = True
                    elif int(self.ll[3].x + 1) == placedblock.x and int(self.ll[3].y) == placedblock.y:
                        self.right_collision = True

                    if int(self.ll[3].y + 1) == placedblock.y and int(self.ll[3].x) == placedblock.x:
                        self.bottom_collision = True
                    elif int(self.ll[0].y + 1) == placedblock.y and int(self.ll[0].x) == placedblock.x:
                        self.bottom_collision = True

            if self.current_rotation == 3:
                for placedblock in self.placed_blocks:
                    if int(self.ll[3].x - 1) == placedblock.x and int(self.ll[3].y) == placedblock.y:
                        self.left_collision = True
                    elif int(self.ll[0].x - 1) == placedblock.x and int(self.ll[0].y) == placedblock.y:
                        self.left_collision = True

                    if int(self.ll[1].x + 1) == placedblock.x and int(self.ll[1].y) == placedblock.y:
                        self.right_collision = True
                    elif int(self.ll[0].x + 1) == placedblock.x and int(self.ll[0].y) == placedblock.y:
                        self.right_collision = True

                    if int(self.ll[0].y + 1) == placedblock.y and int(self.ll[0].x) == placedblock.x:
                        self.bottom_collision = True
                    elif int(self.ll[2].y + 1) == placedblock.y and int(self.ll[2].x) == placedblock.x:
                        self.bottom_collision = True
                    elif int(self.ll[3].y + 1) == placedblock.y and int(self.ll[3].x) == placedblock.x:
                        self.bottom_collision = True

            if self.current_rotation == 4:
                for placedblock in self.placed_blocks:
                    if int(self.ll[0].x - 1) == placedblock.x and int(self.ll[0].y) == placedblock.y:
                        self.left_collision = True
                    elif int(self.ll[2].x - 1) == placedblock.x and int(self.ll[2].y) == placedblock.y:
                        self.left_collision = True
                    elif int(self.ll[3].x - 1) == placedblock.x and int(self.ll[3].y) == placedblock.y:
                        self.left_collision = True

                    if int(self.ll[1].x + 1) == placedblock.x and int(self.ll[1].y) == placedblock.y:
                        self.right_collision = True
                    elif int(self.ll[2].x + 1) == placedblock.x and int(self.ll[2].y) == placedblock.y:
                        self.right_collision = True
                    elif int(self.ll[3].x + 1) == placedblock.x and int(self.ll[3].y) == placedblock.y:
                        self.right_collision = True

                    if int(self.ll[0].y + 1) == placedblock.y and int(self.ll[0].x) == placedblock.x:
                        self.bottom_collision = True
                    if int(self.ll[1].y + 1) == placedblock.y and int(self.ll[1].x) == placedblock.x:
                        self.bottom_collision = True

    def move_block_auto(self):
        self.tick = True

        if self.current_block == 1:
            for block in self.twobytwo:
                if block.y < 19.0 and not self.bottom_collision:
                    block.y += 1
                else:
                    self.block_placed = True
                    self.placed_blocks += self.twobytwo
                    self.current_rotation = 1
                    break

        if self.current_block == 2:
            if self.current_rotation == 1 or self.current_rotation == 2:
                for block in self.ll:
                    if self.ll[3].y < 19.0 and not self.bottom_collision:
                        block.y += 1
                    else:
                        self.block_placed = True
                        self.placed_blocks += self.ll
                        self.current_rotation = 1
                        break

            elif self.current_rotation == 3 or self.current_rotation == 4:
                for block in self.ll:
                    if self.ll[0].y < 20.0 and not self.bottom_collision:
                        block.y += 1
                    else:
                        self.block_placed = True
                        self.placed_blocks += self.ll
                        self.current_rotation = 1
                        break

        self.tick = True

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
        if self.current_block == 1:
            if self.twobytwo[0].x > 5 and self.twobytwo[0].y < 20.0 and not self.left_collision:
                self.twobytwo[0].x -= 1
                self.twobytwo[1].x -= 1
                self.twobytwo[2].x -= 1
                self.twobytwo[3].x -= 1

        if self.current_block == 2:
            if self.ll[0].x > 5 and self.ll[1].y < 20.0 and not self.left_collision:
                self.ll[0].x -= 1
                self.ll[1].x -= 1
                self.ll[2].x -= 1
                self.ll[3].x -= 1

    def move_block_right(self):
        if self.current_block == 1:
            if self.twobytwo[2].x < 14 and self.twobytwo[0].y < 20.0 and not self.right_collision:
                self.twobytwo[0].x += 1
                self.twobytwo[1].x += 1
                self.twobytwo[2].x += 1
                self.twobytwo[3].x += 1

        if self.current_block == 2:
            if self.ll[3].x < 14 and self.ll[1].y < 20.0 and not self.right_collision:
                self.ll[0].x += 1
                self.ll[1].x += 1
                self.ll[2].x += 1
                self.ll[3].x += 1

    def move_block_down(self):
        self.score += 1
        if self.current_block == 1:
            if self.twobytwo[0].y < 19.0 and not self.bottom_collision:
                self.twobytwo[0].y += 1
                self.twobytwo[1].y += 1
                self.twobytwo[2].y += 1
                self.twobytwo[3].y += 1
            else:
                self.block_placed = True
                self.placed_blocks += self.twobytwo
                self.current_rotation = 1

        if self.current_block == 2:
            if self.ll[1].y < 19.0 and not self.bottom_collision:
                self.ll[0].y += 1
                self.ll[1].y += 1
                self.ll[2].y += 1
                self.ll[3].y += 1
            else:
                self.block_placed = True
                self.placed_blocks += self.ll
                self.current_rotation = 1

    def check_row(self):
        # checks for filled rows
        self.x = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        # lots of room for better runtime here...

        #tracks how many blocks are in every row
        for j in range(20):
            for i in range(len(self.placed_blocks)):
                if self.placed_blocks[i].y == j:
                    self.x[j] += self.placed_blocks[i].x

        # reset the vectors of the blocks that are removed
        # if a variable in the list = 95 then this row is full
        for j in range(20):
            for i in range(len(self.placed_blocks)):
                if self.x[j] == 95 and self.placed_blocks[i].y == j:
                    self.placed_blocks[i].x = 0
                    self.placed_blocks[i].y = 0
                    self.blockscleared += 1
                    self.totalblockscleared += 1

        # updates the score for rows cleared
        if self.blockscleared == 10:
            self.score += 40 * (self.level + 1)
            self.firstclear = True
            self.settimerflag = True
        elif self.blockscleared == 20:
            self.score += 100 * (self.level + 1)
            self.firstclear = True
            self.settimerflag = True
        elif self.blockscleared == 30:
            self.score += 300 * (self.level + 1)
            self.firstclear = True
            self.settimerflag = True
        elif self.blockscleared == 40:
            self.score += 1200 * (self.level + 1)
            self.firstclear = True
            self.settimerflag = True

        self.blockscleared = 0

        # level up every 10 rows cleared
        #if (self.level + 1) * 100 == self.totalblockscleared and self.firstclear:
        if (self.totalblockscleared == 10 or self.totalblockscleared == 20) and self.firstclear:
            self.level += 1
            self.firstclear = False

        # let all blocks above the removed row "fall down"
        for j in range(20):
            for i in range(len(self.placed_blocks)):
                if self.x[j] == 95 and j > self.placed_blocks[i].y > 0:
                    self.placed_blocks[i].y += 1
        for j in range(20):
            self.x[j] = 0

    def check_game_over(self):
        for j in range(4):
            for i in range(len(self.placed_blocks)):
                if self.twobytwo[j].x == self.placed_blocks[i].x and self.twobytwo[j].y == self.placed_blocks[i].y:
                    self.placed_blocks = []
                    self.blocksfrozen = True
                    self.score = 0
                    self.level = 0
                    print('game over')
                    break

    def draw_block(self):
        if self.current_block == 1:
            for block in self.twobytwo:
                twobytwo_rect = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size-5, cell_size-5)
                pygame.draw.rect(screen, (250,0,0), twobytwo_rect)
        if self.current_block == 2:
            for block in self.ll:
                ll_rect = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size-5, cell_size-5)
                pygame.draw.rect(screen, (250,0,0), ll_rect)

    def draw_placed_blocks(self):
        for block in self.placed_blocks:
            placed_blocks_rect = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size-5, cell_size-5)
            pygame.draw.rect(screen, (0,240,100), placed_blocks_rect)

    def draw_controls(self):
        controls_text = 'Use A,S,D to move'
        controls_surface = controls_font.render(controls_text, True, (56,74,12))
        controls_x = int(cell_size * cell_count_hor/2)
        controls_y = int(cell_size * cell_count_vert/2) - 150
        controls_rect = controls_surface.get_rect(center = (controls_x, controls_y))

        screen.blit(controls_surface, controls_rect)

    def draw_score(self):
        score_text = 'Score'
        score_num = str(self.score)
        score_surface = score_font.render(score_text, True,(255,255,255))
        score_num_surface = score_num_font.render(score_num, True, (255,255,255))
        score_x = 17.5 * cell_size
        score_y = 2 * cell_size
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        score_num_rect = score_num_surface.get_rect(center=(score_x, score_y + 80))
        background_rect = pygame.rect.Rect(score_rect.left - 90, score_rect.top - 20, 300, 200)

        pygame.draw.rect(screen, (0,0,0), background_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(score_num_surface, score_num_rect)

    def draw_level(self):
        level_text = 'Level'
        level_num = str(self.level)
        level_surface = level_font.render(level_text, True, (255,255,255))
        level_num_surface = level_num_font.render(level_num, True, (255,255,255))
        level_x = 17.5 * cell_size
        level_y = 14 * cell_size
        level_rect = level_surface.get_rect(center=(level_x, level_y))
        level_num_rect = level_num_surface.get_rect(center=(level_x, level_y + 90))
        background_rect = pygame.rect.Rect(level_rect.left - 45, level_rect.top - 20, 200, 200)

        pygame.draw.rect(screen, (0,0,0), background_rect)
        screen.blit(level_surface, level_rect)
        screen.blit(level_num_surface, level_num_rect)

    def draw_next_block(self):
        next_block_text = ' Next'
        next_block_surface = score_num_font.render(next_block_text, True, (255,255,255))
        block_posx = 17.5 * cell_size
        block_posy = 8 * cell_size
        next_block_rect = next_block_surface.get_rect(center=(block_posx, block_posy))
        background_rect = pygame.rect.Rect(next_block_rect.left - 90, next_block_rect.top - 20, 370, 350)

        pygame.draw.rect(screen, (0,0,0), background_rect)
        screen.blit(next_block_surface, next_block_rect)

        if self.next_block == 1:
            for block in self.twobytwo_next:
                twobytwo_rect = pygame.Rect(int((block.x + 8) * cell_size) - 30, int((block.y + 9) * cell_size), cell_size-5, cell_size-5)
                pygame.draw.rect(screen, (250,0,0), twobytwo_rect)
        if self.next_block == 2:
            for block in self.ll_next:
                ll_rect = pygame.Rect(int((block.x + 8) * cell_size) + 20, int((block.y + 9) * cell_size), cell_size-5, cell_size-5)
                pygame.draw.rect(screen, (250,0,0), ll_rect)




class Main():
    def __init__(self):
        self.block = Blocks()
        self.update_call = False

    def update(self):
        self.update_call = True
        if not self.block.block_placed and not self.block.blocksfrozen:
            self.block.move_block_auto()
            self.block.collision_reset()

    def faster_update(self):
        if not self.block.block_placed:
            self.block.check_collision()
            self.block.check_row()
        else:
            self.block.reset()
            self.block.current_block = self.block.next_block
            self.block.next_block = random.randint(1,2)
            self.block.check_game_over()
            self.block.block_placed = False

    def draw_game_elements(self):
        self.block.draw_block()
        self.block.draw_placed_blocks()
        self.draw_sidelines()
        self.block.draw_score()
        self.block.draw_level()
        self.block.draw_next_block()
        if self.block.blocksfrozen:
            self.block.draw_controls()

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
controls_font = pygame.font.Font(None, 90)
score_font = pygame.font.Font(None, 60)
score_num_font = pygame.font.Font(None, 100)
level_font = pygame.font.Font(None, 60)
level_num_font = pygame.font.Font(None, 150)

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
            main.block.blocksfrozen = False
            if event.key == pygame.K_a and not main.block.block_placed:
                main.block.move_block_left()
                main.block.check_collision()
            if event.key == pygame.K_d and not main.block.block_placed:
                main.block.move_block_right()
                main.block.check_collision()
            if event.key == pygame.K_s and not main.block.block_placed:
                main.block.move_block_down()
                main.block.check_collision()
            if event.key == pygame.K_SPACE and not main.block.block_placed:
                # determine the needed rotation and rotate
                print(main.block.current_rotation)
                if main.block.current_block == 1:
                    pass

                elif main.block.current_block == 2:
                    main.block.rotate()
                    if main.block.current_rotation == 4:
                        main.block.current_rotation = 1
                    else:
                        main.block.current_rotation += 1

                elif main.block.current_block == 3:
                    main.block.rotate()
                    if main.block.current_rotation == 4:
                        main.block.current_rotation = 1
                    else:
                        main.block.current_rotation += 1

    if main.block.level == 1 and main.block.settimerflag:
        # settimerflag for the purpose of only calling this timer-update once after a level-up
        pygame.time.set_timer(screen_update, 800)
        main.block.settimerflag = False

    if main.block.level == 2 and main.block.settimerflag:
        pygame.time.set_timer(screen_update, 700)
        main.block.settimerflag = False

    if main.block.level == 3 and main.block.settimerflag:
        pygame.time.set_timer(screen_update, 600)
        main.block.settimerflag = False

    if main.block.level == 4 and main.block.settimerflag:
        pygame.time.set_timer(screen_update, 500)
        main.block.settimerflag = False

    if main.block.level == 5 and main.block.settimerflag:
        pygame.time.set_timer(screen_update, 400)
        main.block.settimerflag = False

    if main.block.level == 6 and main.block.settimerflag:
        pygame.time.set_timer(screen_update, 300)
        main.block.settimerflag = False

    if main.block.level == 7 and main.block.settimerflag:
        pygame.time.set_timer(screen_update, 200)
        main.block.settimerflag = False

    if main.block.level == 8 and main.block.settimerflag:
        pygame.time.set_timer(screen_update, 150)
        main.block.settimerflag = False

    if main.block.level == 9 and main.block.settimerflag:
        pygame.time.set_timer(screen_update, 150)
        main.block.settimerflag = False

    if main.block.level == 10 and main.block.settimerflag:
        pygame.time.set_timer(screen_update, 100)
        main.block.settimerflag = False

    screen.fill((0,0,0))
    main.draw_game_elements()
    main.faster_update()

    pygame.display.update()
    clock.tick(60)
