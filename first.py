#this is the first work file
import pygame
import os
from pygame.locals import *

WIDTH, HEIGHT = 1250,750


pygame.init()

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("HADIS")

DuckX = 100
DuckY = 300
angle = 0
hooked = False

BACKGROUND = pygame.image.load(os.path.join('images', 'BIGGERSpace.png'))
CURSOR = pygame.image.load(os.path.join('images', 'lazerPointTransparent.png'))
DUCK = pygame.image.load(os.path.join('images','yellowDuckTransparent.png'))
CAUGHT = pygame.image.load(os.path.join('images', 'yellow_coughtTransparent.png'))
CAUGHT = pygame.transform.scale(CAUGHT, (140, 140))
DUCK = pygame.transform.scale(DUCK, (100, 100))
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def mouse_on(MX,MY,x,y):
    ok = False
    if(MX>=x+60):
        if(MX<=x+75):
            if(MY>=y):
                if(MY<=y+15):
                    ok = True
    return ok

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

    if (DuckX>(WIDTH+100)): DuckX = -100

    #DUCK = pygame.transform.rotate(DUCK, angle)
    #WIN.blit (CURSOR, (DuckX+70,DuckY+10))

    if(mouse_on(MX,MY,DuckX,DuckY)):
        hooked = True

    if(hooked):
        DuckX = MX-87
        DuckY = MY-18
        WIN.blit(CAUGHT,(DuckX,DuckY))
    else:
        DUCK_COPY = pygame.transform.rotate(DUCK, angle)
        WIN.blit (DUCK_COPY, (DuckX - int(DUCK_COPY.get_width() / 2) , DuckY - int(DUCK_COPY.get_height() / 2)))



    angle = angle + 3

    DuckX = DuckX + 3
    DuckY = DuckY

    pygame.display.flip()

pygame.quit()