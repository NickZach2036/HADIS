
import pygame
import os
from pygame.locals import *

WIDTH, HEIGHT = 1250,750


pygame.init()

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("HADIS")

DuckX = 100
DuckY = 300

BACKGROUND = pygame.image.load(os.path.join('images', 'BIGGERSpace.png'))
CURSOR = pygame.image.load(os.path.join('images', 'lazerPointTransparent.png'))
DUCK = pygame.image.load(os.path.join('images','yellowDuckTransparent.png'))
DUCK = pygame.transform.scale(DUCK, (100, 100))
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

DUCK_MASK = pygame.mask.from_surface(DUCK)
DUCK_RECT = DUCK.get_rect()

CURSOR_MASK = pygame.mask.from_surface(CURSOR)
CURSOR_RECT = CURSOR.get_rect()

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

    WIN.blit(DUCK,(DuckX,DuckY))

    offset = (DuckX-MX, DuckY-MY)
    result = CURSOR_MASK.overlap(DUCK_MASK, offset)

    if result:
        DuckX, DuckY = 0,300
        WIN.blit(DUCK,(DuckX,DuckY))
        
    DuckX = DuckX+1
    pygame.display.flip()

pygame.quit()