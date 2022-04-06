import pygame, math
import pymunk
import pymunk.pygame_util
import os

DUCK = pygame.image.load(os.path.join('images','yellowDuckTransparent.png'))
DUCK = pygame.transform.scale(DUCK, (100, 100))

pygame.init()
screen = pygame.display.set_mode((500, 500))
draw_options = pymunk.pygame_util.DrawOptions(screen)

def create_duck1(space, pos):
    body = pymunk.Body(1, 100, body_type= pymunk.Body.DYNAMIC)
    body.position = pos
    poly_dims = [(65, 20), (75, 20), (90, 70), (75, 95), (20, 95), (0, 70)]
    shape = pymunk.Poly(body,poly_dims)
    space.add(body,shape)
    return shape

def draw_ducks(ducks):
    for duck in ducks:
        pos_x = int(duck.body.position.x)
        pos_y = int(duck.body.position.y)
        screen.blit(DUCK, (pos_x,pos_y))


space = pymunk.Space()
space.gravity = (500, 200)

ducks = []
ducks.append(create_duck1(space, (100, 100)))

clock = pygame.time.Clock()

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((255, 255, 255))
    draw_ducks(ducks)

    # \/ \/ \/ To check the hitboxes, uncommet the following piece of code below:
    space.debug_draw(draw_options)

    space.step(1/50)
    pygame.display.flip()

pygame.quit()