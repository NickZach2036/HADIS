#this is the first work file
import pygame
import os
from pygame.locals import *

WIGHT, HEIGHT = 1250,750


pygame.init()

screen = pygame.display.set_mode([WIGHT, HEIGHT])
pygame.display.set_caption("HADIS")

DuckX = 100
DuckY = 100

BACKGROUND = pygame.image.load(os.path.join('Game pixel art', 'BIGGERSpace.png'))
IMAGE = pygame.image.load(os.path.join('Game pixel art', 'lazerPointTransparent.png'))
DUCK = pygame.image.load(os.path.join('Game pixel art','yellowDuckTransparent.png'))
BIG_DUCK = pygame.transform.scale(DUCK, (100, 100))
WIN = pygame.display.set_mode((WIGHT, HEIGHT))

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

    WIN.blit(BIG_DUCK,(DuckX,DuckY))
    BIG_DUCK = pygame.transform.rotate(BIG_DUCK,-1)
   # if (DuckX>WIGHT): DuckX = -100

   # DuckX = DuckX + 2
   # DuckY = DuckY

    pygame.display.flip()

pygame.quit()