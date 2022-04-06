import pygame
import pygame_menu
import pymunk
import os

pygame.init()

WIDTH = 1366
HEIGHT = 708
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

LOGO = pygame.image.load(os.path.join('Game pixel art', 'logo.png'))
pygame.display.set_icon(LOGO)
pygame.display.set_caption("HADIS")

HADIStheme = pygame_menu.themes.THEME_DARK.copy()
BACKGROUND = pygame_menu.baseimage.BaseImage(image_path=os.path.join('Game pixel art', 'BIGGERSpace.png'), drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
HADIStheme.background_color = BACKGROUND

def music(VALUE, MUSIC):
    if MUSIC:
        pygame.mixer.music.load('Mahalageasca (Bucovina Dub).mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.12)
    else:
        pygame.mixer.music.stop()
    pass

def start_the_game():
    # Do the job here !
    pass

#MAX = 13
#SCORE = 31

def highest_score():
    if (SCORE > MAX):
        MAX = SCORE
    return MAX

def about_page():
    # Do the job here !
    pass

MENU = pygame_menu.Menu('HADIS', WIDTH/2, HEIGHT/2, theme=pygame_menu.themes.THEME_DARK)
MENU.add.button('Play', start_the_game)
MENU.add.selector('Music: ', [('Off', False), ('On', True)], onchange=music)
MENU.add.button('Highest Score', highest_score)
MENU.add.button('About the game', about_page)
MENU.add.button('Quit', pygame_menu.events.EXIT)

MENU.mainloop(SCREEN)