
# one library for the win
import pygame
pygame.init()

# display setup
WIDTH, HEIGHT = 1300, 700
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battleship")
clock = pygame.time.Clock()

# text font
MAIN_FONT = pygame.font.SysFont("comicsans", 80)

# constants
WHITE = (255, 255, 255)
WATER = (14, 128, 229)
SAND = (255, 235, 143)
GRASS = (6, 219, 103)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
FPS = 60


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

    # method to draw ships on mouse position during ship placing stage
    def draw(self, win):
        m_x, m_y = pygame.mouse.get_pos()

        # only draw ship inside the correct board
        if self.bounds[0] < m_x < self.bounds[1] and self.bounds[2] < m_y < self.bounds[3]:
            self.location[0] = self.dir
            self.location[1] = self.segments
            if self.dir == "vertical":
                v100, v75, v50, v25 = 100, 75, 50, 25
                h100, h75, h50, h25 = 0, 0, 0, 0
                xincrement = 0
                yincrement = self.u
            if self.dir == "horizontal":
                v100, v75, v50, v25 = 0, 0, 0, 0
                h100, h75, h50, h25 = 100, 75, 50, 25
                xincrement = self.u
                yincrement = 0

            # adjust bounds for indivisual ship size and orientation
            if self.segments == 5: self.bounds = [self.init_bounds[0] + h100, self.init_bounds[1] - h100, self.init_bounds[2] + v100, self.init_bounds[3] - v100]
            if self.segments == 4: self.bounds = [self.init_bounds[0] + h75, self.init_bounds[1] - h75, self.init_bounds[2] + v75, self.init_bounds[3] - v75]
            if self.segments == 3: self.bounds = [self.init_bounds[0] + h50, self.init_bounds[1] - h50, self.init_bounds[2] + v50, self.init_bounds[3] - v50]
            if self.segments == 2: self.bounds = [self.init_bounds[0] + h25, self.init_bounds[1] - h25, self.init_bounds[2] + v25, self.init_bounds[3] - v25]
            
            # ships with an odd ammount of segments
            if self.segments % 2 == 1:
                h_x, h_y = m_x // self.u * self.u, m_y // self.u * self.u
                self.location[2] = [h_x, h_y]
                rect = pygame.Rect(h_x, h_y, self.u, self.u)
                pygame.draw.rect(win, BLACK, rect, 0)
                for i in range(2):
                    for j in range(self.segments // 2):
                        rect = pygame.Rect(h_x + (xincrement * (j + 1)), h_y + (yincrement * (j + 1)), self.u, self.u)
                        pygame.draw.rect(win, BLACK, rect, 0)
                    xincrement *= -1
                    yincrement *= -1

            # ships with an even ammount of segements
            if self.segments % 2 == 0:
                self.location[2] = [[(m_x - h25) // self.u * self.u, (m_y - v25) // self.u * self.u], [(m_x + h25) // self.u * self.u, (m_y + v25) // self.u * self.u]]
                rect = pygame.Rect((m_x - h25) // self.u * self.u, (m_y - v25) // self.u * self.u, self.u, self.u)
                pygame.draw.rect(win, BLACK, rect, 0)
                rect = pygame.Rect((m_x + h25) // self.u * self.u, (m_y + v25) // self.u * self.u, self.u, self.u)
                pygame.draw.rect(win, BLACK, rect, 0)
                if self.segments == 4:
                    rect = pygame.Rect((m_x - h75) // self.u * self.u, (m_y - v75) // self.u * self.u, self.u, self.u)
                    pygame.draw.rect(win, BLACK, rect, 0)
                    rect = pygame.Rect((m_x + h75) // self.u * self.u, (m_y + v75) // self.u * self.u, self.u, self.u)
                    pygame.draw.rect(win, BLACK, rect, 0)


# coordinate interpreter
def get_ship_tiles(location):
    ship_tile_list = []
    if location[0] == "vertical": v50, v100, h50, h100 = 50, 100, 0, 0
    if location[0] == "horizontal": v50, v100, h50, h100 = 0, 0, 50, 100
    if location[1] == 3 or location[1] == 5:
        ship_tile_list.append((location[2][0], location[2][1]))
        ship_tile_list.append((location[2][0] - h50, location[2][1] - v50))
        ship_tile_list.append((location[2][0] + h50, location[2][1] + v50))
    if location[1] == 2 or location[1] == 4:
        ship_tile_list.append((location[2][0][0], location[2][0][1]))
        ship_tile_list.append((location[2][1][0], location[2][1][1]))
    if location[1] == 5:
        ship_tile_list.append((location[2][0] - h100, location[2][1] - v100))
        ship_tile_list.append((location[2][0] + h100, location[2][1] + v100))
    if location[1] == 4:
        ship_tile_list.append((location[2][0][0] - h50, location[2][0][1] - v50))
        ship_tile_list.append((location[2][1][0] + h50, location[2][1][1] + v50))
    return ship_tile_list


# runs both start and end screens
def run_start_end_screen(startend, winner):
    while True:
        clock.tick(FPS)
        
        # draw start screen
        if startend == "start":
            win.fill(WHITE)

            rule1 = MAIN_FONT.render("NO STACKING/OVERLAPPING SHIPS!", 1, BLACK)
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

        # draw end screen
        if startend == "end":
            win.fill(BLACK)

            game_winner = MAIN_FONT.render(winner, 1, WHITE)
            win.blit(game_winner, (int(WIDTH/2 - game_winner.get_width()/2), 250))
            restart = MAIN_FONT.render("PRESS ENTER TO PLAY AGAIN", 1, WHITE)
            win.blit(restart, (int(WIDTH/2 - restart.get_width()/2), 350))
            pygame.display.update()

        pygame.display.update()

        # common event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run_game()


def draw_game(show_left, show_right, listsList):

    # grid function
    def drawGrid(x, y, blockSize):
        reset = x
        for i in range(10):
            x = reset
            for j in range(10):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(win, WHITE, rect, 1)
                x += blockSize
            y += blockSize

    # static background
    win.fill(SAND)
    pygame.draw.rect(win, GRASS, (75, 75, 550, 550), 0)
    pygame.draw.rect(win, GRASS, (675, 75, 550, 550), 0)
    pygame.draw.rect(win, WATER, (100, 100, 500, 500), 0)
    pygame.draw.rect(win, WATER, (700, 100, 500, 500), 0)
    drawGrid(100, 100, 50)
    drawGrid(700, 100, 50)

    # draw player one's UI
    if show_left:
        for square in listsList[0]:
            pygame.draw.rect(win, BLACK, (square[0], square[1], 50, 50), 0)
        player_one_turn_label = MAIN_FONT.render("Player One's Turn", 1, BLACK)
        win.blit(player_one_turn_label, (int(WIDTH/4 - player_one_turn_label.get_width()/2 + 20), 10))

    # draw player two's UI
    if show_right:
        for square in listsList[1]:
            pygame.draw.rect(win, BLACK, (square[0], square[1], 50, 50), 0)
        player_two_turn_label = MAIN_FONT.render("Player Two's Turn", 1, BLACK)
        win.blit(player_two_turn_label, (int((WIDTH - WIDTH/4) - player_two_turn_label.get_width()/2 - 30), 10))

    # always show both side's hits and misses
    for i in range(2):
        for square in listsList[i + 2]:
            pygame.draw.rect(win, RED, (square[0], square[1], 50, 50), 0)
    for j in range(2):
        for square in listsList[j + 4]:
            pygame.draw.rect(win, BLUE, (square[0], square[1], 50, 50), 0)


def run_game():

    # player one ships
    p1_five = Ship(5, 50, [100, 600, 100, 600], "left")
    p1_four = Ship(4, 50, [100, 600, 100, 600], "left")
    p1_three1 = Ship(3, 50, [100, 600, 100, 600], "left")
    p1_three2 = Ship(3, 50, [100, 600, 100, 600], "left")
    p1_two = Ship(2, 50, [100, 600, 100, 600], "left")

    # player two ships
    p2_five = Ship(5, 50, [700, 1200, 100, 600], "right")
    p2_four = Ship(4, 50, [700, 1200, 100, 600], "right")
    p2_three1 = Ship(3, 50, [700, 1200, 100, 600], "right")
    p2_three2 = Ship(3, 50, [700, 1200, 100, 600], "right")
    p2_two = Ship(2, 50, [700, 1200, 100, 600], "right")

    # ship list to iterate through during ship placing stage
    ships = [p1_five, p1_four, p1_three1, p1_three2, p1_two,
    p2_five, p2_four, p2_three1, p2_three2, p2_two]

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

        # main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            # handle ship rotations
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    if placing_stage < 10:
                        ships[placing_stage].rotate()

            # handle ship placing and shooting
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # <<< left click

                    # get clicked square coordinates
                    m_x, m_y = pygame.mouse.get_pos()
                    h_x, h_y = m_x // 50 * 50, m_y // 50 * 50

                    # ship placing stage
                    if placing_stage < 4:
                        for ship_tile in get_ship_tiles(ships[placing_stage].location):
                            left_ship_tile_list.append(ship_tile)
                        placing_stage += 1
                    elif placing_stage == 4:
                        show_left = False
                        show_right = True
                        for ship_tile in get_ship_tiles(ships[placing_stage].location):
                            left_ship_tile_list.append(ship_tile)
                        placing_stage += 1
                    elif placing_stage < 10:
                        for ship_tile in get_ship_tiles(ships[placing_stage].location):
                            right_ship_tile_list.append(ship_tile)

                        # set cursor to broken_x for gameplay stage
                        if placing_stage == 9: pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                        placing_stage += 1

                    else: # gameplay stage

                        # variable to change turn when appropriate
                        change = True

                        # prevent suicidal shots
                        if show_right:
                            if 100 <= h_x < 600 and 100 <= h_y < 600:

                                # disallow players to shoot where they already have shot
                                if (h_x, h_y) not in left_hit_tile_list and (h_x, h_y) not in left_miss_tile_list:
                                    if (h_x, h_y) in left_ship_tile_list:
                                        left_hit_tile_list.append((h_x, h_y))
                                    else:
                                        left_miss_tile_list.append((h_x, h_y))
                                else:
                                    change = False
                            else:
                                change = False

                        # prevent suicidal shots
                        if show_left:
                            if 700 <= h_x < 1200 and 100 <= h_y < 600:
                                if (h_x, h_y) not in right_hit_tile_list and (h_x, h_y) not in right_miss_tile_list:
                                    if (h_x, h_y) in right_ship_tile_list:
                                        right_hit_tile_list.append((h_x, h_y))
                                    else:
                                        right_miss_tile_list.append((h_x, h_y))
                                else:
                                    change = False
                            else:
                                change = False

                        # change board visibility for new turn
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
                            win.blit(waiting_label, (int(WIDTH/2 - waiting_label.get_width()/2), 640))
                            pygame.display.update()
                            pygame.time.wait(3000)


if __name__ == '__main__':
    run_start_end_screen("start", '')
