
import pygame
import os
from pygame.locals import *
import math

WIDTH, HEIGHT = 1250,750


pygame.init()

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("HADIS")

DuckX = 100
DuckY = 100
angle = 0
angleBox = 0

BACKGROUND = pygame.image.load(os.path.join('images', 'BIGGERSpace.png'))
CURSOR = pygame.image.load(os.path.join('images', 'lazerPointTransparent.png'))
CAUGHT = pygame.image.load(os.path.join('images', 'yellow_coughtTransparent.png'))
CAUGHT = pygame.transform.scale(CAUGHT, (140, 140))
DUCK = pygame.image.load(os.path.join('images','yellowDuckTransparent.png'))
DUCK = pygame.transform.scale(DUCK, (100, 100))
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

DUCK_MASK = pygame.mask.from_surface(DUCK)

CURSOR_MASK = pygame.mask.from_surface(CURSOR)

def mouse_on(MX,MY,x,y):
    ok = False
    if(MX>=x+60):
        if(MX<=x+77):
            if(MY>=y-4):
                if(MY<=y+17):
                    ok = True
    return ok

hooked = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    WIN.fill((0,0,0))
    WIN.blit(BACKGROUND, (0,0))

    MX, MY = pygame.mouse.get_pos()
    WIN.blit(CURSOR, (MX-3,MY-3))
    pygame.mouse.set_visible(False)

    offset = (DuckX-MX, DuckY-MY)
    result = CURSOR_MASK.overlap(DUCK_MASK, offset)


    #antenaX,antenaY = (DuckX+7), (DuckY-55)

    if(mouse_on(MX,MY,DuckX,DuckY)):
        hooked = True


    if hooked:
        DuckX = MX-87
        DuckY = MY-18
        WIN.blit(CAUGHT,(DuckX,DuckY))
    else:
        if result:
            DuckX, DuckY = 0,300
            WIN.blit(DUCK,(DuckX,DuckY))
        else:
            WIN.blit(DUCK,(DuckX,DuckY))
            DuckX = DuckX+2

            '''
            DUCK_COPY = pygame.transform.rotate(DUCK, angle)
            DuckRotX = DuckX - int(DUCK_COPY.get_width() / 2)
            DuckRotY = DuckY - int(DUCK_COPY.get_height() / 2)

            pygame.draw.rect (WIN, (255,0,0),[(antenaX*math.cos(angleBox) + 70),(antenaY*math.sin(angleBox) + 30), 17, 17])
            angleBox = angleBox + 0.01

            
            WIN.blit (DUCK_COPY, (DuckRotX, DuckRotY))

            if (angle == 360):
                angle = 0
            else:
                angle = angle + 3
                DuckX = DuckX+2
            
            print(angle)'''



    pygame.display.flip()

pygame.quit()