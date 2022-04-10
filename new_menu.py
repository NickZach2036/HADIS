import pygame
import pygame_menu
import pymunk
import os
import time

pygame.init()

WIDTH, HEIGHT = 1250, 750

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

LOGO = pygame.image.load(os.path.join('images', 'logo.png'))
pygame.display.set_icon(LOGO)
pygame.display.set_caption("HADIS")

HADIStheme = pygame_menu.themes.THEME_DARK.copy()
BACKGROUND = pygame_menu.baseimage.BaseImage(image_path=os.path.join('images', 'BIGGERSpace.png'), drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
HADIStheme.background_color = BACKGROUND

def music(VALUE, MUSIC):
    if MUSIC:
        pygame.mixer.music.load('Mahalageasca_Bucovina_Dub.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.12)
    else:
        pygame.mixer.music.stop()

def start_the_game():
    import pygame, pymunk, os, random

    BACKGROUND = pygame.image.load(os.path.join('images', 'BIGGERSpace.png'))
    BASKET = pygame.image.load(os.path.join('images', 'CatchBasketT.png'))
    OVERBASKET = pygame.image.load(os.path.join('images', 'OverBasket.png'))

    DUCK = pygame.image.load(os.path.join('images', 'yellowDuckTransparent.png'))
    DUCK = pygame.transform.scale(DUCK, (100, 100))

    CAUGHT = pygame.image.load(os.path.join('images', 'yellow_coughtTransparent.png'))
    CAUGHT = pygame.transform.scale(CAUGHT, (140, 140))

    CURSOR = pygame.image.load(os.path.join('images', 'lazerPointTransparent.png'))

    space = pymunk.Space()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font('SofiaSanswdthwght.ttf',32)

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

            self.antena_dims = [(5, -55), (30,-55), (30,-30), (5,-30)]
            self.antenaShape = pymunk.Poly(self.body, self.antena_dims)
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
        shape = pymunk.Circle(body, 3)
        shape.elasticity = 1
        shape.filter = pymunk.ShapeFilter(group=1)
        space.add(body, shape)
        return shape

    def CursorDraw(cursor):
        pos_x = int(cursor.body.position.x)
        pos_y = int(cursor.body.position.y)
        screen.blit(CURSOR, (pos_x - 3, pos_y - 3))

    def Caught(space):
        body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        body.position = ((WIDTH + 300), (HEIGHT + 300))
        shape = pymunk.Circle(body, 3)
        shape.elasticity = 1
        space.add(body, shape)

        return shape

    def hookCheck(ducks, MX, MY):
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

    def activeDucks(ducks):
        activeCurrently = 0
        for duck in ducks:
            if (duck.active):
                activeCurrently = activeCurrently + 1

        done = True

        if (activeCurrently < 10):
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


    pygame.init()
    
    ducks = []
    for i in range(15):
        duck1 = Duck(space, ((WIDTH + 300), (HEIGHT + 300)))
        ducks.append(duck1)

    Lazer = Cursor(space, (0, 0))
    caught = Caught(space)

    hooked = False
    points = 0

    currentTime = 0
    gameStart = 0

    countDown = 3

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        currentTime = pygame.time.get_ticks()

        pygame.mouse.set_visible(False)

        screen.fill((0, 0, 0))
        screen.blit(BACKGROUND, (0, 0))

        if(countDown > 0):
            count = font.render(str(countDown), True, (255,0,0))
            screen.blit(count, (WIDTH/2, HEIGHT/2))

            time.sleep(1)
            countDown -= 1
            if (countDown == 0):
                gameStart = pygame.time.get_ticks()

        else: 
            #leftTime = 60 - ((currentTime - gameStart) - (currentTime - gameStart)%1000)
            #if(leftTime > 0):
                MX, MY = pygame.mouse.get_pos()
                MX = MX - 3
                MY = MY - 3
                Lazer.body.position = (MX, MY)
                CursorDraw(Lazer)

                if (hookCheck(ducks, MX, MY)):
                    hooked = True

                ducks = outOfBoundsCheck(ducks)

                ducks = activeDucks(ducks)

                draw_ducks(ducks)

                screen.blit(BASKET, (0, 300))

                if (hooked):
                    DuckX = MX - 87
                    DuckY = MY - 18
                    caught.body.position = (DuckX, DuckY)
                    screen.blit(CAUGHT, (DuckX, DuckY))
                    if (DuckY > 650):
                        hooked = False
                        duckpp = getPoints(ducks)
                        points += duckpp

                # make the ilusion that the duck goes into the ship
                screen.blit(OVERBASKET, (0, HEIGHT - 12))

                showScore(points,10,10)

        space.step(1 / 50)
        pygame.display.update()
        clock.tick(120)


#MAX = 13
#SCORE = 31

"""def highest_score():
    if (SCORE > MAX):
        MAX = SCORE
    return MAX"""

def about_page():
    # Do the job here !
    pass

MENU = pygame_menu.Menu('HADIS', WIDTH/2, HEIGHT/2, theme=pygame_menu.themes.THEME_DARK)
MENU.add.button('Play', start_the_game)
MENU.add.selector('Music: ', [('Off', False), ('On', True)], onchange=music)
#MENU.add.button('Highest Score', highest_score)
MENU.add.button('About the game', about_page)
MENU.add.button('Quit', pygame_menu.events.EXIT)

MENU.mainloop(SCREEN)