import pygame, pygame_menu

pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)

scl = []
hgscl = [0, 0, 0, 0, 0] #Първоначалн0 всички резултати са нули, после започва да се пълни с новите score-ове

score = 0 #някакво произволно число, реших да е пак 0, щото шо не

scl.append(score)
scl.sort()

hgscl = scl[:5]