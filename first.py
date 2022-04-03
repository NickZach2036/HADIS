#this is the first work file
import pygame
import os
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode([1000, 500])
pygame.display.set_caption("HADIS")

BACKGROUND = pygame.image.load(os.path.join('images', 'BIGGERSpace.png'))
IMAGE = pygame.image.load(os.path.join('images', 'lazerPointTransparent.png'))
WIN = pygame.display.set_mode((1000, 500))

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

    pygame.display.flip()

pygame.quit()