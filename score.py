import pygame

pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

textsurface = myfont.render('Some Text', False, (0, 0, 0))

screen.blit(textsurface,(0,0))

pygame.display.update()