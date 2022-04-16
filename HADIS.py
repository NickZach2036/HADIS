from dis import Instruction
from tracemalloc import start
import pygame
import pygame_menu
import pymunk
import os
import time
from datetime import date, datetime

pygame.init()

WIDTH, HEIGHT = 1250, 750

screen = pygame.display.set_mode((WIDTH, HEIGHT))

BACKGROUND = pygame.image.load(os.path.join('images', 'BIGGERSpace.png'))

TEXT = pygame.image.load(os.path.join('images', 'about.png'))
TEXT = pygame.transform.scale(TEXT, (1250, 750))

HIGH_SCORE_BG = pygame.image.load(os.path.join('images', 'HSB.png'))
PAUSE = pygame.image.load(os.path.join('images', 'Pause_Menu.jpg'))

font = pygame.font.Font('SofiaSanswdthwght.ttf',32)
ScoreFont = pygame.font.Font('SofiaSanswdthwght.ttf',54)
InitialsFont = pygame.font.Font('SofiaSanswdthwght.ttf',48)

LOGO = pygame.image.load(os.path.join('images', 'logo.png'))
pygame.display.set_icon(LOGO)
pygame.display.set_caption("HADIS")

def music(VALUE, MUSIC):
    if MUSIC:
        pygame.mixer.music.load('Mahalageasca_Bucovina_Dub.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.12)
    else:
        pygame.mixer.music.stop()

def high_score_bg():
    Masiv = []
    textFile = open ("top5.txt", "r")
    for line in textFile:
        info = [ item.strip() for item in line.split(',')]
        Masiv.append(info)
    textFile.close()

    for i in range(len(Masiv)):
        Masiv[i][0] = int(Masiv[i][0])

    Masiv.sort(reverse=True)

    for i in range(len(Masiv)):
        Masiv[i][0] = str(Masiv[i][0])

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(HIGH_SCORE_BG, (0, 0))
        line = ''
        offset = 0
        for i in range(10):
            showNumber = i + 1
            number = str(showNumber)
            line = number + '. ' + Masiv[i][1] + ' - ' + Masiv[i][0]
            print = font.render(line, True, (255,0,0))
            screen.blit(print, (WIDTH/2.4,250+offset))
            offset += 35


        pygame.display.update()

def start_the_game():
    import pygame, pymunk, os, random

    BASKET = pygame.image.load(os.path.join('images', 'CatchBasketT.png'))
    OVERBASKET = pygame.image.load(os.path.join('images', 'OverBasket.png'))

    DUCK = pygame.image.load(os.path.join('images', 'yellowDuckTransparent.png'))
    DUCK = pygame.transform.scale(DUCK, (100, 100))

    CAUGHT = pygame.image.load(os.path.join('images', 'yellow_coughtTransparent.png'))
    CAUGHT = pygame.transform.scale(CAUGHT, (140, 140))

    CURSOR = pygame.image.load(os.path.join('images', 'lazerPointTransparent.png'))
    CURSOR = pygame.transform.scale(CURSOR, (14, 14))

    BACKTOMENU = pygame.image.load(os.path.join('images', 'backToMenu.png'))
    BACKTOMENU = pygame.transform.scale(BACKTOMENU, (150,50))

    space = pymunk.Space()
    clock = pygame.time.Clock()
    spawnTime = 0

    class Duck:
        def __init__(self, space, pos):
            self.space = space
            self.body = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)
            self.body.position = pos
            self.poly_dims = [(15, -30), (25, -30), (40, 15), (40, 35), (30, 45), (-25, 45), (-45, 15)]
            self.shape = pymunk.Poly(self.body, self.poly_dims)
            self.body.velocity = (400, 0)
            self.shape.elasticity = 1
            self.space.add(self.body, self.shape)

            #self.antena_dims = [(5, -55), (30,-55), (30,-30), (5,-30)]
            self.antenaShape = pymunk.Circle(self.body, 12, (17,-43))
            self.antenaShape.filter = pymunk.ShapeFilter(group=1)
            self.space.add(self.antenaShape)

            self.hooked = False

            self.active = False

            self.points = 10

    def draw_ducks(ducks):
        for duck in ducks:
            if duck.active:
                pos_x = int(duck.body.position.x)
                pos_y = int(duck.body.position.y)

                #rotate the duck and convert radians into degrees
                DUCK_COPY = pygame.transform.rotate(DUCK, (-duck.body.angle*57.2958))
                screen.blit (DUCK_COPY, (pos_x - int(DUCK_COPY.get_width() / 2) , pos_y - int(DUCK_COPY.get_height() / 2)))

    def Cursor(space, pos):
        body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        body.position = pos
        shape = pymunk.Circle(body, 5)
        shape.elasticity = 1
        shape.filter = pymunk.ShapeFilter(group=1)
        space.add(body, shape)
        return shape

    def CursorDraw(cursor):
        pos_x = int(cursor.body.position.x)
        pos_y = int(cursor.body.position.y)
        screen.blit(CURSOR, (pos_x - 7, pos_y - 7))

    def hookCheck(ducks):
        hooked = False
        for duck in ducks:
            x = duck.body.position.x
            y = duck.body.position.y
            if ((duck.antenaShape.shapes_collide(Lazer)).points != [] ):
                duck.active = False
                duck.hooked = True
                hooked = True
                duck.body.position = ((WIDTH + 300), (HEIGHT + 300))
        return hooked

    def outOfBoundsCheck(ducks):
        for duck in ducks:
            if (duck.body.position.x > (WIDTH + 300)):
                duck.active = False
            if (duck.body.position.y > (HEIGHT + 300)):
                duck.active = False
        return ducks

    def activeDucks(ducks,sec):
        activeCurrently = 0
        for duck in ducks:
            if (duck.active):
                activeCurrently = activeCurrently + 1

        done = True
        max = -1
        max += sec
        if(max>10):
            max = 10


        if (activeCurrently < max):
            for duck in ducks:
                if done:
                    if (duck.active == False):
                        duck.active = True
                        pos = ((-100), (random.uniform(50, (HEIGHT - 100))))
                        duck.body.position = pos
                        duck.body.velocity = (400, 0)
                        duck.body.angle = 0
                        duck.body.rotational_vector = (1.0, 0.0)
                        done = False

        return ducks

    def getPoints(ducks):
        points = 0
        for duck in ducks:
            if (duck.hooked == True):
                duck.hooked = False
                points = duck.points
        return points

    def showScore(points,x,y):
        score = font.render(str(points), True, (255,255,51))
        screen.blit(score, (x,y))
        
    def showTimeLeft(sec):
        sec = 60 - sec
        secs = font.render(str(sec), True, (255,0,0))
        screen.blit(secs, (WIDTH-50,10))

    pygame.init()
    
    ducks = []
    for i in range(15):
        duck1 = Duck(space, ((WIDTH + 300), (HEIGHT + 300)))
        ducks.append(duck1)

    Lazer = Cursor(space, (0, 0))

    hooked = False
    points = 0
    countDown = 3

    currentTime = datetime.now()
    oneTimeVariable = True
    runOngoing = True

    userName = ''

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        currentTime = datetime.now()

        pygame.mouse.set_visible(False)

        screen.fill((0, 0, 0))
        screen.blit(BACKGROUND, (0, 0))

        if(countDown >= 0):
            count = font.render(str(countDown), True, (255,0,0))
            screen.blit(count, (WIDTH/2, HEIGHT/2))

            time.sleep(1)
            countDown -= 1

        else:
            if(runOngoing): 
                MX, MY = pygame.mouse.get_pos()
                MX = MX - 3
                MY = MY - 3
                Lazer.body.position = (MX, MY)
                CursorDraw(Lazer)

                if oneTimeVariable:
                    startTime = datetime.now()
                    oneTimeVariable = False
                    
                diff = currentTime - startTime
                sec = diff.seconds

                if(hooked == False):
                    if (hookCheck(ducks)):
                        hooked = True

                ducks = outOfBoundsCheck(ducks)

                ducks = activeDucks(ducks, sec)

                draw_ducks(ducks)

                screen.blit(BASKET, (0, 300))

                if (hooked):
                    DuckX = MX - 89
                    DuckY = MY - 20
                    screen.blit(CAUGHT, (DuckX, DuckY))
                    if (DuckY > 650):
                        hooked = False
                        duckpp = getPoints(ducks)
                        points += duckpp

                    # make the ilusion that the duck goes into the ship
                screen.blit(OVERBASKET, (0, HEIGHT - 12))

                showScore(points,10,10)

                showTimeLeft(sec)

                if(20-sec==0):
                    runOngoing= False
            else:
                screen.blit(PAUSE, (0, 0))
                showScore(points, 650, 138)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            userName = userName[:-1]
                        else: 
                            userName += event.unicode
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if(MX>=200):
                            if(MX<=1050):
                                if(MY>=450):
                                    if(MY<=550):
                                        score = str(points)

                                        file = open('top5.txt', 'a')

                                        file.write(score)
                                        file.write(", ")
                                        file.write(userName)
                                        file.write("\n")

                                        file.close()

                                        running = False

                    '''if event.type == pygame.MOUSEBUTTONDOWN:
                        if(MX>=675):
                            if(MX<=1050):
                                if(MY>=450):
                                    if(MY<=550):
                                        score = str(points)

                                        file = open('top5.txt', 'a')

                                        file.write(score)
                                        file.write(", ")
                                        file.write(userName)
                                        file.write("\n")

                                        file.close()

                                        start_the_game()'''

                if(len(userName)>3):
                    userName = userName[:3]

                name = font.render(userName, True, (255,255,255))
                screen.blit(name,(750,313))
                MX, MY = pygame.mouse.get_pos()
                MX = MX - 3
                MY = MY - 3

                Lazer.body.position = (MX, MY)
                CursorDraw(Lazer)

        space.step(1 / 50)
        pygame.display.update()
        clock.tick(120)

def about_page():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(BACKGROUND, (0, 0))
        screen.blit(TEXT, (0, 0))

        pygame.display.update()
    pass

MENU = pygame_menu.Menu('HADIS', WIDTH/1.5, HEIGHT/1.5, theme=pygame_menu.themes.THEME_DARK)
MENU.add.button('Play', start_the_game)
MENU.add.selector('Music: ', [('Off', False), ('On', True)], onchange=music)
MENU.add.button('Highest Score', high_score_bg) 
MENU.add.button('About the game', about_page)
MENU.add.button('Quit', pygame_menu.events.EXIT)

MENU.mainloop(screen)

pygame.display.update()