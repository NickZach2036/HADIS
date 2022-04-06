import pygame,pymunk,os

DUCK = pygame.image.load(os.path.join('images','yellowDuckTransparent.png'))
DUCK = pygame.transform.scale(DUCK, (100, 100))
CURSOR = pygame.image.load(os.path.join('images', 'lazerPointTransparent.png'))


def create_duck1(space, pos):
    body = pymunk.Body(1, 100, body_type= pymunk.Body.DYNAMIC)
    body.position = pos
    poly_dims = [(65, 20), (75, 20), (90, 70), (75, 95), (20, 95), (0, 70)]
    shape = pymunk.Poly(body,poly_dims)
    shape.elasticity = 1
    space.add(body,shape)
    return shape

def draw_ducks(ducks):
    for duck in ducks:
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


pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = 500,0

ducks = []
ducks.append(create_duck1(space, (0, 400)))

Lazer = Cursor(space,(0,0))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.mouse.set_visible(False)
    

    screen.fill((217,217,217))
    draw_ducks(ducks)
    MX, MY = pygame.mouse.get_pos()
    MX = MX - 3
    MY = MY - 3
    Lazer.body.position = (MX, MY)
    CursorDraw(Lazer)

    space.step(1/50)
    pygame.display.update()
    clock.tick(120)