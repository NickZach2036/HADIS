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

BACKGROUND = pygame.image.load(os.path.join('images', 'BIGGERSpace.png'))
IMAGE = pygame.image.load(os.path.join('images', 'lazerPointTransparent.png'))
DUCK = pygame.image.load(os.path.join('images','yellowDuckTransparent.png'))
BIG_DUCK = pygame.transform.scale(DUCK, (100, 100))
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    WIN.fill((0,0,0))
    WIN.blit(BACKGROUND, (0,0))

    MX, MY = pygame.mouse.get_pos()
    WIN.blit(IMAGE, (MX-3,MY-3))
    pygame.mouse.set_visible(False)

    #WIN.blit(BIG_DUCK,(DuckX,DuckY))
    if (DuckX>(WIDTH+100)): DuckX = -100

    BIG_DUCK_COPY = pygame.transform.rotate(BIG_DUCK, angle)
    WIN.blit (BIG_DUCK_COPY, (DuckX - int(BIG_DUCK_COPY.get_width() / 2) , DuckY - int(BIG_DUCK_COPY.get_height() / 2)))
    angle = angle + 10

    DuckX = DuckX + 3
    DuckY = DuckY

    pygame.display.flip()

pygame.quit()