
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

# coordinate translator
def get_coords(location):
    ship_tile_list = []
    if location[0] == "vertical":
        if location[1] == 3 or location[1] == 5:
            ship_tile_list.append((location[2][0], location[2][1]))
            ship_tile_list.append((location[2][0], location[2][1] - 50))
            ship_tile_list.append((location[2][0], location[2][1] + 50))
        if location[1] == 2 or location[1] == 4:
            ship_tile_list.append((location[2][0][0], location[2][0][1]))
            ship_tile_list.append((location[2][1][0], location[2][1][1]))
        if location[1] == 5:
            ship_tile_list.append((location[2][0], location[2][1] - 100))
            ship_tile_list.append((location[2][0], location[2][1] + 100))
        if location[1] == 4:
            ship_tile_list.append((location[2][0][0], location[2][0][1] - 50))
            ship_tile_list.append((location[2][1][0], location[2][1][1] + 50))
    if location[0] == "horizontal":
        if location[1] == 3 or location[1] == 5:
            ship_tile_list.append((location[2][0], location[2][1]))
            ship_tile_list.append((location[2][0] - 50, location[2][1]))
            ship_tile_list.append((location[2][0] + 50, location[2][1]))
        if location[1] == 2 or location[1] == 4:
            ship_tile_list.append((location[2][0][0], location[2][0][1]))
            ship_tile_list.append((location[2][1][0], location[2][1][1]))
        if location[1] == 5:
            ship_tile_list.append((location[2][0] - 100, location[2][1]))
            ship_tile_list.append((location[2][0] + 100, location[2][1]))
        if location[1] == 4:
            ship_tile_list.append((location[2][0][0] - 50, location[2][0][1]))
            ship_tile_list.append((location[2][1][0] + 50, location[2][1][1]))
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
            pygame.draw.rect(win, BLACK, (square[0], square[1], 50, 50), 0)
    if show_right:
        for square in listsList[1]:
            pygame.draw.rect(win, BLACK, (square[0], square[1], 50, 50), 0)

    for i in range(2):
        for square in listsList[i + 2]:
            pygame.draw.rect(win, RED, (square[0], square[1], 50, 50), 0)
    for j in range(2):
        for square in listsList[j + 4]:
            pygame.draw.rect(win, BLUE, (square[0], square[1], 50, 50), 0)

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
                                if (h_x, h_y) not in left_hit_tile_list and (h_x, h_y) not in left_miss_tile_list:
                                    if (h_x, h_y) in left_ship_tile_list:
                                        left_hit_tile_list.append((h_x, h_y))
                                    else:
                                        left_miss_tile_list.append((h_x, h_y))
                                else:
                                    change = False
                            else:
                                change = False
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
