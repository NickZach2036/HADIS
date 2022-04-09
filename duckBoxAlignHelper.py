from tokenize import group
import pygame, math
import pymunk
import pymunk.pygame_util
import os

DUCK = pygame.image.load(os.path.join('images','yellowDuckTransparent.png'))
DUCK = pygame.transform.scale(DUCK, (100, 100))
CURSOR = pygame.image.load(os.path.join('images', 'lazerPointTransparent.png'))

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
draw_options = pymunk.pygame_util.DrawOptions(screen)

def create_duck1(space, pos):
    body = pymunk.Body(1, 100, body_type= pymunk.Body.DYNAMIC)
    body.position = pos
    body.mass = 0.1
    poly_dims = [(15, -30), (25, -30), (40, 15), (40, 35), (30, 45), (-25, 45), (-45, 15)]
    shape = pymunk.Poly(body,poly_dims)
    body.velocity = (0,0)
    space.add(body,shape)

    antena_dims = [(5, -55), (30,-55), (30,-30), (5,-30)]
    antenaShape = pymunk.Poly(body, antena_dims)
    antenaShape.filter = pymunk.ShapeFilter(group=1)
    space.add(antenaShape)

    return antenaShape

def draw_ducks(ducks):
    for duck in ducks:
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

def offScreenHelpingShape(space):
    body = pymunk.Body(1, 100, body_type= pymunk.Body.DYNAMIC)
    body.position = (2000,2000)
    shape = pymunk.Circle(body,3)
    space.add(body, shape)
    return shape

space = pymunk.Space()
#space.gravity = (400, 1000)
space.damping = 1.1

ducks = []
ducks.append(create_duck1(space, (100, 100)))

Lazer = Cursor(space, (0, 0))

oshs = offScreenHelpingShape(space)

clock = pygame.time.Clock()

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((255, 255, 255))
    draw_ducks(ducks)

    if((ducks[0].shapes_collide(Lazer)).points != [] ):
        print('COLLISION!')


    # \/ \/ \/ To check the hitboxes, uncommet the following piece of code below:
    space.debug_draw(draw_options)

    MX, MY = pygame.mouse.get_pos()
    Lazer.body.position = (MX, MY)
    CursorDraw(Lazer)

    space.step(1/50)
    pygame.display.flip()

pygame.quit()