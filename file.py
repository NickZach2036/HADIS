import pygame, pygame_menu

pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)

hgscl = [0, 0, 0, 0, 0] #Първоначалн0 всички резултати са нули, после започва да се пълни с новите score-ове

score = 0 #някакво произволно число, реших да е пак 0, щото шо не

if score >= hgscl[0]:
    hgscl[4] = hgscl[3]
    hgscl[3] = hgscl[2]
    hgscl[2] = hgscl[1]
    hgscl[1] = hgscl[0]
    hgscl[0] = score
elif score >= hgscl[1]:
    hgscl[4] = hgscl[3]
    hgscl[3] = hgscl[2]
    hgscl[2] = hgscl[1]
    hgscl[1] = score
elif score >= hgscl[2]:
    hgscl[4] = hgscl[3]
    hgscl[3] = hgscl[2]
    hgscl[2] = score
elif score >= hgscl[3]:
    hgscl[4] = hgscl[3]
    hgscl[3] = score
elif score >= hgscl[4]:
    hgscl[4] = score

pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)

textsurface = myfont.render('Some Text', False, (0, 0, 0))

for itr in hgscl:
  screen.blit(textsurface,(0,0))

pygame.display.update() 