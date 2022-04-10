import pygame, pymunk, os, random

BACKGROUND = pygame.image.load(os.path.join('images', 'BIGGERSpace.png'))

DUCK = pygame.image.load(os.path.join('images','yellowDuckTransparent.png'))
DUCK = pygame.transform.scale(DUCK, (100, 100))

CAUGHT = pygame.image.load(os.path.join('images', 'yellow_coughtTransparent.png'))
CAUGHT = pygame.transform.scale(CAUGHT, (140, 140))

CURSOR = pygame.image.load(os.path.join('images', 'lazerPointTransparent.png'))

WIDTH, HEIGHT = 1250,750
space = pymunk.Space()
#space.gravity = 1000,10
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Duck:
    def __init__(self, space, pos):
        self.space = space
        self.body = pymunk.Body(1, 100, body_type = pymunk.Body.DYNAMIC)
        self.body.position = pos
        self.poly_dims = [(65, 20), (75, 20), (90, 60), (90, 85), (75, 95), (20, 95), (0, 70)]
        self.shape = pymunk.Poly(self.body,self.poly_dims)
        self.body.velocity = (100, 0)
        self.shape.elasticity = 1
        self.space.add(self.body,self.shape)

        self.active = False

        self.points = 10

def draw_ducks(ducks):
    for duck in ducks:
        if duck.active:
            pos_x = int(duck.body.position.x)
            pos_y = int(duck.body.position.y)
            screen.blit(DUCK, (pos_x,pos_y))

def Cursor(space,pos):
    body = pymunk.Body(body_type = pymunk.Body.KINEMATIC)
    body.position = pos
    shape = pymunk.Circle(body,3)
    space.add(body,shape)
    shape.elasticity = 1
    return shape

def CursorDraw(cursor):
    pos_x = int(cursor.body.position.x)
    pos_y = int(cursor.body.position.y)
    screen.blit(CURSOR, (pos_x,pos_y))

def mouse_on(MX,MY,x,y):
    ok = False
    if(MX>=x+60):
        if(MX<=x+77):
            if(MY>=y-4):
                if(MY<=y+17):
                    ok = True
    return ok

def hookCheck(ducks,MX,MY):
    hooked = False
    for duck in ducks:
        x = duck.body.position.x
        y = duck.body.position.y
        if mouse_on(MX,MY,x,y):
            duck.active = False
            hooked = True
            duck.body.position = ((WIDTH+300),(HEIGHT+300))
    return hooked

def outOfBoundsCheck(ducks):
    for duck in ducks:
        if (duck.body.position.x > (WIDTH+300)):
            duck.active = False
        if (duck.body.position.y > (HEIGHT+300)):
            duck.active = False
    return ducks

def activeDucks(ducks):
    activeCurrently = 0
    for duck in ducks:
        if (duck.active):
            activeCurrently = activeCurrently + 1

    done = True

    if (activeCurrently<10):
        for duck in ducks:
            if done:
                if (duck.active == False):
                    duck.active = True
                    pos = ((-100),(random.uniform(50,(HEIGHT-50))))
                    duck.body.position = pos
                    done = False
    return ducks
            

ducks = []

for i in range(1):
    duck1=Duck(space, ( (WIDTH+300), (HEIGHT+300) ) )
    ducks.append(duck1)

hooked = False

pygame.init()

Lazer = Cursor(space,(0,0))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.mouse.set_visible(False)
    

    screen.fill((0,0,0))
    screen.blit(BACKGROUND, (0,0))

    MX, MY = pygame.mouse.get_pos()
    MX = MX - 3
    MY = MY - 3
    Lazer.body.position = (MX, MY)

    if(hookCheck(ducks,MX,MY)):
        hooked = True
    
    ducks = outOfBoundsCheck(ducks)

    ducks = activeDucks(ducks)

    draw_ducks(ducks)

    if(hooked):
        DuckX = MX-87
        DuckY = MY-18
        screen.blit(CAUGHT,(DuckX,DuckY))

    CursorDraw(Lazer)

    space.step(1/50)
    pygame.display.update()
    clock.tick(120)