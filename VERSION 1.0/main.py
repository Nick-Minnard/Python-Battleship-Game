
# one library for the win
import pygame
pygame.init()

# display setup
WIDTH, HEIGHT = 1300, 700
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battleship")
clock = pygame.time.Clock()

# constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BG = (141, 206, 216)
FPS = 60

# font(s)
MAIN_FONT = pygame.font.SysFont("comicsans", 80)

# coordinate key
key = {
    'a0': (100, 550), 'a1': (150, 550), 'a2': (200, 550), 'a3': (250, 550), 'a4': (300, 550),
    'a5': (350, 550), 'a6': (400, 550), 'a7': (450, 550), 'a8': (500, 550), 'a9': (550, 550),
    'b0': (100, 500), 'b1': (150, 500), 'b2': (200, 500), 'b3': (250, 500), 'b4': (300, 500),
    'b5': (350, 500), 'b6': (400, 500), 'b7': (450, 500), 'b8': (500, 500), 'b9': (550, 500),
    'c0': (100, 450), 'c1': (150, 450), 'c2': (200, 450), 'c3': (250, 450), 'c4': (300, 450),
    'c5': (350, 450), 'c6': (400, 450), 'c7': (450, 450), 'c8': (500, 450), 'c9': (550, 450),
    'd0': (100, 400), 'd1': (150, 400), 'd2': (200, 400), 'd3': (250, 400), 'd4': (300, 400),
    'd5': (350, 400), 'd6': (400, 400), 'd7': (450, 400), 'd8': (500, 400), 'd9': (550, 400),
    'e0': (100, 350), 'e1': (150, 350), 'e2': (200, 350), 'e3': (250, 350), 'e4': (300, 350),
    'e5': (350, 350), 'e6': (400, 350), 'e7': (450, 350), 'e8': (500, 350), 'e9': (550, 350),
    'f0': (100, 300), 'f1': (150, 300), 'f2': (200, 300), 'f3': (250, 300), 'f4': (300, 300),
    'f5': (350, 300), 'f6': (400, 300), 'f7': (450, 300), 'f8': (500, 300), 'f9': (550, 300),
    'g0': (100, 250), 'g1': (150, 250), 'g2': (200, 250), 'g3': (250, 250), 'g4': (300, 250),
    'g5': (350, 250), 'g6': (400, 250), 'g7': (450, 250), 'g8': (500, 250), 'g9': (550, 250),
    'h0': (100, 200), 'h1': (150, 200), 'h2': (200, 200), 'h3': (250, 200), 'h4': (300, 200),
    'h5': (350, 200), 'h6': (400, 200), 'h7': (450, 200), 'h8': (500, 200), 'h9': (550, 200),
    'i0': (100, 150), 'i1': (150, 150), 'i2': (200, 150), 'i3': (250, 150), 'i4': (300, 150),
    'i5': (350, 150), 'i6': (400, 150), 'i7': (450, 150), 'i8': (500, 150), 'i9': (550, 150),
    'j0': (100, 100), 'j1': (150, 100), 'j2': (200, 100), 'j3': (250, 100), 'j4': (300, 100),
    'j5': (350, 100), 'j6': (400, 100), 'j7': (450, 100), 'j8': (500, 100), 'j9': (550, 100),
    'k0': (700, 550), 'k1': (750, 550), 'k2': (800, 550), 'k3': (850, 550), 'k4': (900, 550),
    'k5': (950, 550), 'k6': (1000, 550), 'k7': (1050, 550), 'k8': (1100, 550), 'k9': (1150, 550),
    'l0': (700, 500), 'l1': (750, 500), 'l2': (800, 500), 'l3': (850, 500), 'l4': (900, 500),
    'l5': (950, 500), 'l6': (1000, 500), 'l7': (1050, 500), 'l8': (1100, 500), 'l9': (1150, 500),
    'm0': (700, 450), 'm1': (750, 450), 'm2': (800, 450), 'm3': (850, 450), 'm4': (900, 450),
    'm5': (950, 450), 'm6': (1000, 450), 'm7': (1050, 450), 'm8': (1100, 450), 'm9': (1150, 450),
    'n0': (700, 400), 'n1': (750, 400), 'n2': (800, 400), 'n3': (850, 400), 'n4': (900, 400),
    'n5': (950, 400), 'n6': (1000, 400), 'n7': (1050, 400), 'n8': (1100, 400), 'n9': (1150, 400),
    'o0': (700, 350), 'o1': (750, 350), 'o2': (800, 350), 'o3': (850, 350), 'o4': (900, 350),
    'o5': (950, 350), 'o6': (1000, 350), 'o7': (1050, 350), 'o8': (1100, 350), 'o9': (1150, 350),
    'p0': (700, 300), 'p1': (750, 300), 'p2': (800, 300), 'p3': (850, 300), 'p4': (900, 300),
    'p5': (950, 300), 'p6': (1000, 300), 'p7': (1050, 300), 'p8': (1100, 300), 'p9': (1150, 300),
    'q0': (700, 250), 'q1': (750, 250), 'q2': (800, 250), 'q3': (850, 250), 'q4': (900, 250),
    'q5': (950, 250), 'q6': (1000, 250), 'q7': (1050, 250), 'q8': (1100, 250), 'q9': (1150, 250),
    'r0': (700, 200), 'r1': (750, 200), 'r2': (800, 200), 'r3': (850, 200), 'r4': (900, 200),
    'r5': (950, 200), 'r6': (1000, 200), 'r7': (1050, 200), 'r8': (1100, 200), 'r9': (1150, 200),
    's0': (700, 150), 's1': (750, 150), 's2': (800, 150), 's3': (850, 150), 's4': (900, 150),
    's5': (950, 150), 's6': (1000, 150), 's7': (1050, 150), 's8': (1100, 150), 's9': (1150, 150),
    't0': (700, 100), 't1': (750, 100), 't2': (800, 100), 't3': (850, 100), 't4': (900, 100),
    't5': (950, 100), 't6': (1000, 100), 't7': (1050, 100), 't8': (1100, 100), 't9': (1150, 100)
}

# key lists for getting key from value \/
key_list = list(key.keys()) # print(key_list[val_list.index((1000, 100))])
val_list = list(key.values()) # print(key['t5'])

# coordinate translator
def get_coords(location):
    ship_tile_list = []
    if location[0] == "vertical":
        if location[1] == 3 or location[1] == 5:
            ship_tile_list.append(key_list[val_list.index((location[2][0], location[2][1]))])
            ship_tile_list.append(key_list[val_list.index((location[2][0], location[2][1] - 50))])
            ship_tile_list.append(key_list[val_list.index((location[2][0], location[2][1] + 50))])
        if location[1] == 2 or location[1] == 4:
            ship_tile_list.append(key_list[val_list.index((location[2][0][0], location[2][0][1]))])
            ship_tile_list.append(key_list[val_list.index((location[2][1][0], location[2][1][1]))])
        if location[1] == 5:
            ship_tile_list.append(key_list[val_list.index((location[2][0], location[2][1] - 100))])
            ship_tile_list.append(key_list[val_list.index((location[2][0], location[2][1] + 100))])
        if location[1] == 4:
            ship_tile_list.append(key_list[val_list.index((location[2][0][0], location[2][0][1] - 50))])
            ship_tile_list.append(key_list[val_list.index((location[2][1][0], location[2][1][1] + 50))])
    if location[0] == "horizontal":
        if location[1] == 3 or location[1] == 5:
            ship_tile_list.append(key_list[val_list.index((location[2][0], location[2][1]))])
            ship_tile_list.append(key_list[val_list.index((location[2][0] - 50, location[2][1]))])
            ship_tile_list.append(key_list[val_list.index((location[2][0] + 50, location[2][1]))])
        if location[1] == 2 or location[1] == 4:
            ship_tile_list.append(key_list[val_list.index((location[2][0][0], location[2][0][1]))])
            ship_tile_list.append(key_list[val_list.index((location[2][1][0], location[2][1][1]))])
        if location[1] == 5:
            ship_tile_list.append(key_list[val_list.index((location[2][0] - 100, location[2][1]))])
            ship_tile_list.append(key_list[val_list.index((location[2][0] + 100, location[2][1]))])
        if location[1] == 4:
            ship_tile_list.append(key_list[val_list.index((location[2][0][0] - 50, location[2][0][1]))])
            ship_tile_list.append(key_list[val_list.index((location[2][1][0] + 50, location[2][1][1]))])
    return ship_tile_list

# ship class
class Ship:

    # constructor
    def __init__(self, segments, blockSize, bounds, side):
        self.init_bounds = bounds
        self.bounds = bounds
        self.segments = segments
        self.u = blockSize
        self.dir = "vertical"
        self.side = side
        self.location = [0, 0, 0] # direction, segments, base coord(s)

    # ship placing stage rotation feature
    def rotate(self):
        if self.dir == "vertical": self.dir = "horizontal"
        else: self.dir = "vertical"

    # this method is too long and it knows it
    def draw(self, win):
        increment = self.u
        m_x, m_y = pygame.mouse.get_pos()
        if self.side == "left" or self.side == "right":
            if self.bounds[0] < m_x < self.bounds[1] and self.bounds[2] < m_y < self.bounds[3]:
                self.location[1] = self.segments
                if self.dir == "vertical":
                    self.location[0] = "vertical"
                    if self.segments == 5: self.bounds = [self.init_bounds[0], self.init_bounds[1], self.init_bounds[2] + 100, self.init_bounds[3] - 100]
                    if self.segments == 4: self.bounds = [self.init_bounds[0], self.init_bounds[1], self.init_bounds[2] + 75, self.init_bounds[3] - 75]
                    if self.segments == 3: self.bounds = [self.init_bounds[0], self.init_bounds[1], self.init_bounds[2] + 50, self.init_bounds[3] - 50]
                    if self.segments == 2: self.bounds = [self.init_bounds[0], self.init_bounds[1], self.init_bounds[2] + 25, self.init_bounds[3] - 25]
                    if self.segments % 2 == 1:
                        h_x, h_y = m_x // self.u * self.u, m_y // self.u * self.u
                        self.location[2] = [h_x, h_y]
                        rect = pygame.Rect(h_x, h_y, self.u, self.u)
                        pygame.draw.rect(win, BLACK, rect, 0)
                        for i in range(2):
                            for j in range(self.segments // 2):
                                rect = pygame.Rect(h_x, h_y + (increment * (j + 1)), self.u, self.u)
                                pygame.draw.rect(win, BLACK, rect, 0)
                            increment *= -1
                    if self.segments % 2 == 0:
                        self.location[2] = [[m_x // self.u * self.u, (m_y - 25) // self.u * self.u],
                        [m_x // self.u * self.u, (m_y + 25) // self.u * self.u]]
                        rect = pygame.Rect(m_x // self.u * self.u, (m_y - 25) // self.u * self.u, self.u, self.u)
                        pygame.draw.rect(win, BLACK, rect, 0)
                        rect = pygame.Rect(m_x // self.u * self.u, (m_y + 25) // self.u * self.u, self.u, self.u)
                        pygame.draw.rect(win, BLACK, rect, 0)
                        if self.segments == 4:
                            rect = pygame.Rect(m_x // self.u * self.u, (m_y - 75) // self.u * self.u, self.u, self.u)
                            pygame.draw.rect(win, BLACK, rect, 0)
                            rect = pygame.Rect(m_x // self.u * self.u, (m_y + 75) // self.u * self.u, self.u, self.u)
                            pygame.draw.rect(win, BLACK, rect, 0)
                if self.dir == "horizontal":
                    self.location[0] = "horizontal"
                    if self.segments == 5: self.bounds = [self.init_bounds[0] + 100, self.init_bounds[1] - 100, self.init_bounds[2], self.init_bounds[3]]
                    if self.segments == 4: self.bounds = [self.init_bounds[0] + 75, self.init_bounds[1] - 75, self.init_bounds[2], self.init_bounds[3]]
                    if self.segments == 3: self.bounds = [self.init_bounds[0] + 50, self.init_bounds[1] - 50, self.init_bounds[2], self.init_bounds[3]]
                    if self.segments == 2: self.bounds = [self.init_bounds[0] + 25, self.init_bounds[1] - 25, self.init_bounds[2], self.init_bounds[3]]
                    if self.segments % 2 == 1:
                        h_x, h_y = m_x // self.u * self.u, m_y // self.u * self.u
                        self.location[2] = [h_x, h_y]
                        rect = pygame.Rect(h_x, h_y, self.u, self.u)
                        pygame.draw.rect(win, BLACK, rect, 0)
                        for i in range(2):
                            for j in range(self.segments // 2):
                                rect = pygame.Rect(h_x + (increment * (j + 1)), h_y, self.u, self.u)
                                pygame.draw.rect(win, BLACK, rect, 0)
                            increment *= -1
                    if self.segments % 2 == 0:
                        self.location[2] = [[(m_x - 25) // self.u * self.u, m_y // self.u * self.u], [(m_x + 25) // self.u * self.u, m_y // self.u * self.u]]
                        rect = pygame.Rect((m_x - 25) // self.u * self.u, m_y // self.u * self.u, self.u, self.u)
                        pygame.draw.rect(win, BLACK, rect, 0)
                        rect = pygame.Rect((m_x + 25) // self.u * self.u, m_y // self.u * self.u, self.u, self.u)
                        pygame.draw.rect(win, BLACK, rect, 0)
                        if self.segments == 4:
                            rect = pygame.Rect((m_x - 75) // self.u * self.u, m_y // self.u * self.u, self.u, self.u)
                            pygame.draw.rect(win, BLACK, rect, 0)
                            rect = pygame.Rect((m_x + 75) // self.u * self.u, m_y // self.u * self.u, self.u, self.u)
                            pygame.draw.rect(win, BLACK, rect, 0)

# ships
p1_five = Ship(5, 50, [100, 600, 100, 600], "left")
p1_four = Ship(4, 50, [100, 600, 100, 600], "left")
p1_three1 = Ship(3, 50, [100, 600, 100, 600], "left")
p1_three2 = Ship(3, 50, [100, 600, 100, 600], "left")
p1_two = Ship(2, 50, [100, 600, 100, 600], "left")

p2_five = Ship(5, 50, [700, 1200, 100, 600], "right")
p2_four = Ship(4, 50, [700, 1200, 100, 600], "right")
p2_three1 = Ship(3, 50, [700, 1200, 100, 600], "right")
p2_three2 = Ship(3, 50, [700, 1200, 100, 600], "right")
p2_two = Ship(2, 50, [700, 1200, 100, 600], "right")

ships = [p1_five, p1_four, p1_three1, p1_three2, p1_two,
p2_five, p2_four, p2_three1, p2_three2, p2_two]


# runs both start and end screens \/
def run_start_end_screen(startend, winner):
    while True:
        clock.tick(FPS)
        
        if startend == "start":
            win.fill(WHITE)

            rule1 = MAIN_FONT.render("NO STACKING SHIPS", 1, BLACK)
            win.blit(rule1, (int(WIDTH/2 - rule1.get_width()/2), 75))
            rule2 = MAIN_FONT.render("3 SECONDS IN BETWEEN TURNS", 1, BLACK)
            win.blit(rule2, (int(WIDTH/2 - rule2.get_width()/2), 175))
            rule3 = MAIN_FONT.render("PRESS \'r\' TO ROTATE A SHIP", 1, BLACK)
            win.blit(rule3, (int(WIDTH/2 - rule3.get_width()/2), 275))
            rule4 = MAIN_FONT.render("RED = HIT", 1, BLACK)
            win.blit(rule4, (int(WIDTH/2 - rule4.get_width()/2), 375))
            rule5 = MAIN_FONT.render("BLUE = MISS", 1, BLACK)
            win.blit(rule5, (int(WIDTH/2 - rule5.get_width()/2), 475))
            rule6 = MAIN_FONT.render("PRESS ENTER TO START", 1, BLACK)
            win.blit(rule6, (int(WIDTH/2 - rule6.get_width()/2), 575))
        if startend == "end":
            win.fill(BLACK)

            game_winner = MAIN_FONT.render(winner, 1, WHITE)
            win.blit(game_winner, (int(WIDTH/2 - game_winner.get_width()/2), 250))
            restart = MAIN_FONT.render("PRESS ENTER TO PLAY AGAIN", 1, WHITE)
            win.blit(restart, (int(WIDTH/2 - restart.get_width()/2), 350))
            pygame.display.update()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run_game()


def draw_game(show_left, show_right, listsList):

    # custom grid function
    def drawGrid(x, y, blockSize):
        reset = x
        for i in range(10):
            x = reset
            for j in range(10):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(win, WHITE, rect, 1)
                x += blockSize
            y += blockSize

    win.fill(BG)

    drawGrid(100, 100, 50)
    drawGrid(700, 100, 50)

    if show_left:
        for square in listsList[0]:
            pygame.draw.rect(win, BLACK, (key[square][0], key[square][1], 50, 50), 0)
    if show_right:
        for square in listsList[1]:
            pygame.draw.rect(win, BLACK, (key[square][0], key[square][1], 50, 50), 0)

    for i in range(2):
        for square in listsList[i + 2]:
            pygame.draw.rect(win, RED, (key[square][0], key[square][1], 50, 50), 0)
    for j in range(2):
        for square in listsList[j + 4]:
            pygame.draw.rect(win, BLUE, (key[square][0], key[square][1], 50, 50), 0)

def run_game():

    # game specific variables
    show_left = True
    show_right = False
    left_ship_tile_list = []
    right_ship_tile_list = []
    left_hit_tile_list = []
    right_hit_tile_list = []
    left_miss_tile_list = []
    right_miss_tile_list = []
    listsList = [left_ship_tile_list, right_ship_tile_list, left_hit_tile_list,
    right_hit_tile_list, left_miss_tile_list,right_miss_tile_list]
    placing_stage = 0

    while True:
        clock.tick(FPS)
        draw_game(show_left, show_right, listsList)
        if placing_stage < 10:
            ships[placing_stage].draw(win)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    if placing_stage < 10:
                        ships[placing_stage].rotate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # <<< left click

                    # get clicked square coordinates
                    m_x, m_y = pygame.mouse.get_pos()
                    h_x, h_y = m_x // 50 * 50, m_y // 50 * 50

                    # ship placing stage
                    if placing_stage < 4:
                        for coord in get_coords(ships[placing_stage].location):
                            left_ship_tile_list.append(coord)
                        placing_stage += 1
                    elif placing_stage == 4:
                        show_left = False
                        show_right = True
                        for coord in get_coords(ships[placing_stage].location):
                            left_ship_tile_list.append(coord)
                        placing_stage += 1
                    elif placing_stage < 10:
                        for coord in get_coords(ships[placing_stage].location):
                            right_ship_tile_list.append(coord)
                        placing_stage += 1

                    # gameplay stage
                    else:

                        # change variable exists to make the program do nothing
                        # if a player didn't click a grid tile
                        change = True
                        if show_right:
                            if 100 <= h_x < 600 and 100 <= h_y < 600:
                                if key_list[val_list.index((h_x, h_y))] not in left_hit_tile_list and key_list[val_list.index((h_x, h_y))] not in left_miss_tile_list:
                                    if key_list[val_list.index((h_x, h_y))] in left_ship_tile_list:
                                        left_hit_tile_list.append(key_list[val_list.index((h_x, h_y))])
                                    else:
                                        left_miss_tile_list.append(key_list[val_list.index((h_x, h_y))])
                                else:
                                    change = False
                            else:
                                change = False
                        if show_left:
                            if 700 <= h_x < 1200 and 100 <= h_y < 600:
                                if key_list[val_list.index((h_x, h_y))] not in right_hit_tile_list and key_list[val_list.index((h_x, h_y))] not in right_miss_tile_list:
                                    if key_list[val_list.index((h_x, h_y))] in right_ship_tile_list:
                                        right_hit_tile_list.append(key_list[val_list.index((h_x, h_y))])
                                    else:
                                        right_miss_tile_list.append(key_list[val_list.index((h_x, h_y))])
                                else:
                                    change = False
                            else:
                                change = False
                        if change:
                            if show_left:
                                show_left = False
                                show_right = True
                            else:
                                show_left = True
                                show_right = False

                            # check for gameover
                            if len(left_hit_tile_list) >= 17:
                                run_start_end_screen("end", 'RIGHT WINS!')
                            if len(right_hit_tile_list) >= 17:
                                run_start_end_screen("end", 'LEFT WINS!')

                            # change turns in 3 seconds
                            waiting_label = MAIN_FONT.render("Your Turn is Done! Look Away!", 1, BLACK)
                            win.blit(waiting_label, (int(WIDTH/2 - waiting_label.get_width()/2), 625))
                            pygame.display.update()
                            pygame.time.wait(3000)


if __name__ == '__main__':
    run_start_end_screen("start", '')
